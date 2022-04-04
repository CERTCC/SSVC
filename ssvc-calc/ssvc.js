/* SSVC code for graph building */
const _version = "5.1.4"
const _tool = "Dryad SSVC Calculator "+_version
var showFullTree = false
var diagonal,tree,svg,duration,root
var treeData = []
/* Deefault color array of possible color options */
var acolors = ["#28a745","#ffc107","#EE8733","#dc3545","#ff0000","#aa0000","#ff0000"]
var lcolors = {"Track":"#28a745","Track*":"#ffc107","Attend":"#EE8733","Act":"#dc3545"}
var ssvc_short_keys = {};
/* These variables are for decision tree schema JSON aka SSVC Provision Schema */
var export_schema = {decision_points: [],decisions_table: [], lang: "en",
		     version: "2.0", title: "SSVC Provision table"}
/* If a new analysis is being done use this for export */
var current_score = [];
var current_tree = "CISA-Coordinator-v2.0.3.json";
var roll_tree_map = {"CISA-Coordinator" : "CISA-Coordinator-v2.0.3.json",
		     "Supplier": "Supplier-v2.0.0.json",
		     "Deployer": "Deployer-v2.0.0.json",
		     "Coordinator-Publish": "Coordinator-Publish-v2.0.0.json",
		     "Coordinator-Triage": "Coordinator-Triage-v2.0.0.json"
		    };
var current_schema = "SSVC_Computed_v2.03.schema.json";
/* A dictionary of elements that are children of a decision point*/
var ischild = {};
var isparent = {};

/* Default keyword for final step in the tree will be Decision with 
   class .Decision for rendering */
var final_keyword = "Decision";
/* Outcome of the final decision when a SSVC value has been calculated*/
var final_outcome = "Unknown";

/* Extend jQuery to support simulate D3 click events */
jQuery.fn.simClick = function () {
    this.each(function (i, e) {
	var evt = new MouseEvent("click");
	e.dispatchEvent(evt);
    });
};
function reset_form() {
    /* This is to clear stupid Firefox cached form values*/
    $('select').prop('selectedIndex',0);	    
    $('input[type="file"]').hide();
    $('input').val('');
    $('select').prop('selectedIndex',0);
    $('input[type="file"]').hide();
}
function select_add_option(s,opt) {
    var q = s.find('option').toArray().findIndex(function(x) {
	if(x.value == opt) {
	    x.selected = true;
	    return true; }
    });
    if(q < 0) {
	s.append($('<option/>').
		 attr({value: opt,selected: true})
		 .html(opt));
    };
}
$(function () {
    reset_form();
    Object.keys(roll_tree_map).forEach(function(x) {
	var display = roll_tree_map[x].replace(".json","");
	$('#tree_samples').append($('<option>')
				  .attr({value:roll_tree_map[x]})
				  .html(display))
    });
    $('#topalert').width($('main').width());
    window.onresize = function() { $('#topalert').width($('main').width())}
    $('[data-toggle="tooltip"]').tooltip();
    if(localStorage.getItem("beenhere")) {
	tooltip_cycle_through();
    } else {
	$('#helper').show();
	localStorage.setItem("beenhere",1);
    }
    //load_tsv_score();
    //tree_process("CISA-Coordinator-v2.01.json");
    if(location.hash != "") {
	/*  IF location specifies are tree and its valid, preload the right tree
	   "SSVCv2/E:A/V:S/T:T/M:H/D:C/1632171335/&CVE-2014-01-01&Coordinator" 
	*/	
	var lparts = location.hash.substr(1).split("&");
	if((lparts.length > 1) && (lparts[1] in roll_tree_map)) {
	    current_tree = roll_tree_map[lparts[1]];
	    $('#tree_samples').val(current_tree);
	    select_add_option($('.export'),lparts[1]);
	}
	/* For some reason when .val() is used the cloning of this export does not
	 carry over the value .attr of "value" works right */
	if((lparts.length > 2) && (lparts[2] != "")) 
	    $('.exportId').attr("value",lparts[2]);
    }
    select_add_option($('#tree_samples'),current_tree);    
    $.getJSON(current_tree).done(function(idata) {
	parse_json(idata);
    }).fail(function() {
	console.log("Failed to Load CISA tree.  Loading default tree");
    });
    export_tree();
    load_tsv_score();
})
var raw = [];

document.onkeyup = function(evt) {
    evt = evt || window.event;
    if (evt.keyCode == 27) {
	console.log("Escape hit")
	$('.tescape').fadeOut()
    }
}
function cve_table_toggle() {
    $('#cve_table').toggleClass('d-none')
    if($('#cve_table').hasClass('d-none'))
	$('#table_toggle').html("&#8853;")
    else
	$('#table_toggle').html("&#8854;")
}
function tooltip_cycle_through() {
    var tips = ['#dt_start','#dt_full_tree','#dt_clear']
    $(tips[0]).tooltip('show')
    var itip =1
    var ix = setInterval(function() {
	$('button').tooltip('hide')
	$(tips[itip]).tooltip('show')
	itip++
	if(itip > tips.length) {
	    clearInterval(ix)
	    $('button').tooltip('dispose')
	}
    },1300)

}
function dynamic_mwb(w) {
    var mwbid = $(w).data('tid');
    var pmwbid = '#'+mwbid;
    var mpdata = $(pmwbid).data('parent');
    var mcdata = {}
    $(pmwbid+' select').each(
	(i,k)  => {
	    var opchoice = $(k).val();
	    var cdata = $(k).data('moptions');
	    if('label' in cdata) {
		/* Global variable for export then local var*/
		var tscore = {};
		tscore[cdata['label']] = opchoice;
		mcdata[cdata['label']] = opchoice;
		current_score.push(tscore);
	    } else {
		console.log("Error cannot find relationship information with label");
	    }
	});
    var keys_match = Object.keys(mcdata).length
    var result = "Unknown/Error";
    var soptions = mpdata.options
    find_score:
    for(var i=0; i<soptions.length; i++) {
	if('child_combinations' in soptions[i]) {
	    var spt = soptions[i]['child_combinations'];
	    for(var j=0; j<spt.length; j++) {
		var current_match = {};
		for(var k=0; k < spt[j].length; k++) {
		    if(('child_label' in spt[j][k]) && (spt[j][k].child_label in mcdata)) {
			var spk = spt[j][k]
			var myopt = mcdata[spt[j][k].child_label];
			if(spk.child_option_labels.findIndex(
			    x => x == myopt) > -1) {
			    current_match[spt[j][k].child_label] = 1;
			    if(Object.keys(current_match).length == keys_match) {
				result = soptions[i].label;
				break find_score;
			    }
			}
		    }
		}
	    }
	}
    }
    $(pmwbid+' .wscore').html(result);
    $(pmwbid+' .wsdiv').show();
    $('circle[nameid="'+result.toLowerCase()+'"]').parent().simClick();
    $(pmwbid+' .wsdiv').fadeOut('slow');
    setTimeout(function() {
	$('.complex').modal('hide');
    }, 400);
    return result;
}
function export_show(novector) {
    var ptranslate = "translate(120,-250)";
    if(window.innerWidth <= 1000)
	ptranslate = "translate(30,-90) scale(0.4,0.4)";
    d3.select("#pgroup").transition()
	.duration(600).attr("transform", ptranslate);
    var q = $('#exporter').html()
    $('#graph').append(q)
    if($('#cve_samples').val().match(/^(cve|vu)/i))
	$('.exportId').val($('#cve_samples').val())
    if(novector == true)
	return
    setTimeout(make_ssvc_vector,1000);
}
function make_ssvc_vector() {
    console.log($('.exportId').val());
    var tstamp = new Date()
    var labels = current_score.map(x => Object.keys(x)[0]);
    var vals = current_score.map((x,i) => x[labels[i]]);
    labels.push(final_keyword);
    /* last node in graph */
    var final_outcome =  $('#graph svg g.node text:last').text();
    vals.push(final_outcome);
    /* SSVCv2/Ps:Nm/T:T/U:E/1605040000/
       For a vulnerability with no or minor Public Safety Impact, 
       total Technical Impact, and efficient Utility, 
       which was evaluated on Nov 10, 2020. */
    var computed = "SSVCv2/"
    var ochoice =  labels.map((k, i) => {
	var ox = {}
	ox[k] = vals[i]
	var lhs = k[0].toUpperCase()
	if (k in ssvc_short_keys)
	    lhs = ssvc_short_keys[k]
	var rhs = vals[i][0].toUpperCase()
	if(vals[i] in ssvc_short_keys)
	    rhs = ssvc_short_keys[vals[i]]
	computed = computed + lhs+":"+rhs+"/"
	return ox
    })
    /* Save the ochoice object for Export to JSON*/
    $('#graph .Exporter').attr('data-ochoice',JSON.stringify(ochoice))
    /* new Time string will be ISO 8601 "2021-09-28T21:46:38Z"
       q=new Date().toISOString().replace(/\..*$/,'Z') */
    //computed = computed + String(parseInt(tstamp.getTime()/1000))+"/"
    var q = new Date().toISOString().replace(/\..*$/,'Z');
    computed = computed+q+"/"
    $('.ssvcvector').html(computed);
}    
function export_tree() {
    /* First column is the decision in this tree */
    var toptions = []
    var yhead = [final_keyword]
    var yprops = {}
    export_schema.decisions_table = raw.filter(x => {
	if (x.name.split(":").length > 4)
	    return true
	else {
	    var t = x.name.split(":")[0]
	    if(!(t in yprops)) {
		yprops[t] = 1
		yhead.push(t)
	    }
	    return false
	}
    }).map(x => x.name.split(":").
	   reduce((z,y,i) => {
	       z[yhead[i]] = y
	       if(!toptions[i]) {
		   toptions[i] = [{label: y, description: y}]
	       }
	       else if (!toptions[i].find(t => t.label == y))
		   toptions[i].push({label: y, description:y})
	       return z
	   },{}))
    /* Now the decision points should be moved to the end of the array */
    yhead.push(yhead.shift())
    toptions.push(toptions.shift())
    export_schema.decision_points = yhead.map((a,i) => {
	var ax = {label: a, decision_type: "simple", options: toptions[i]}
	return ax
    })
    //console.log(toptions)
    //export_schema.decisions = tdecisions.map((x,i) => Object.assign(x,{color: acolors[i]}))
    /*
      export_schema.decisions = Object.keys(tdecisions).map((n,i) => {
      return {label: n, description: n, color:acolors[i]}})
    */
    //return allrows;
    /* "[{"Exploitation":"none"},{"Utility":"partial"},
       {"TechnicalImpact":"laborious"},{"SafetyImpact":"none"},
       {"Decision":"defer"}]" */
}
function export_json() {
    var includetree = $('#graph .includetree').is(':checked')
    $('.Exporter').css({'pointer-events':'none'});
    var tstamp = new Date()
    var oexport = { role: $('#graph .exportRole').val() || "Unknown",
		    id: $('#graph .exportId').val() || "Unspecified",
		    version: "2.0",
		    generator: _tool
		  }
    oexport['computed'] = $('#graph .ssvcvector').html();
    
    oexport['timestamp'] =  $('#graph .ssvcvector').html().split('/').
	slice(-2,-1)[0]
    final_outcome = $('#graph svg g.node text:last').text();
    /* Copy current_score as is to options that were selected */
    oexport['options'] = current_score;
    var last_option = {};
    last_option[final_keyword] = final_outcome;
    oexport['options'].push(last_option);
    oexport['$schema'] = location.origin + location.pathname + current_schema
    oexport['decision_tree_url'] = location.origin + location.pathname +
	current_tree;
    var a = document.createElement("a")
    var download_filename = oexport.id+"_"+oexport.role+"_json.txt"
    if (includetree) {
	oexport['decision_tree'] = export_schema
	download_filename = "tree_and_path-"+ oexport.id + "_" + oexport.role +
	    "_json.txt"	
    } 
    a.href = "data:text/plain;charset=utf-8,"+
	encodeURIComponent(JSON.stringify(oexport,null,2))
    a.setAttribute("download", download_filename)
    a.click()
    a.remove()
    $('.Exporter').css({'pointer-events':'all'});    
}

function readFile(input) {
    var file = input.files[0];
    var reader = new FileReader();
    //console.log(file)
    reader.readAsText(file);
    reader.onload = function() {
	//console.log(reader)
	//console.log(reader.result);
	try {
	    if(input.id == "dtreecsvload") {
		select_add_option($('#tree_samples'),file.name);
		if(file.name.match(/\.json$/i))
		    parse_json(reader.result)
		else
		    parse_file(reader.result)
	    }
	    else
		tsv_load(reader.result)
	}catch(err) {
	    reset_form();
	    topalert("Reading data in file as text failed, Sorry check format"+
		     " and try again!","danger")
	    console.log(err)
	}
    };
    
    reader.onerror = function() {
	console.log(reader.error);
	topalert("Reading data in file as text failed","danger")
    };
    
}
function topalert(msg,level) {
    if(!level)
	level = "info"
    var mw = $('#topalert').parent().width()
    $('#topalert').width(String(mw)+"px");
    $('#topalert').html(msg).removeClass().addClass("alert alert-"+level,msg).fadeIn("fast",function() {
	$(this).delay(2000).fadeOut("slow"); })
}
function tree_process(w) {
    var ptree = $(w).val()
    if(ptree == "import") {
	if(navigator.userAgent.indexOf("Chrome") < 0) {
	    $('#dtreecsvload').show()
	    $('#dtreecsvload').click()
	    topalert("Choose the file to upload below")
	} else 
	    $('#dtreecsvload').click()
	return
    }
    $.get(ptree, function(idata) {
        if(ptree.match(/\.json$/i))
	    parse_json(idata)
	else
	    parse_file(idata)
	/* remove .json from the name. This method uses the file name */
	var ptree_name = ptree.replace(/\.[^\.]+$/,'')
	$('.cover_heading_append').html('('+ptree_name+')');
    })
}
function create_permalink(copyme){
    $('.permalink').removeClass('d-none');
    var purl = location.origin+location.pathname+"#"+
	$("#graph .ssvcvector").html()
    var uparts = [".ssvcvector",".exportId",".exportRole"]
    for (var i=0; i<uparts.length; i++) {
	if($("#graph "+uparts[i]).val()) {
	    purl = purl +"&"+$("#graph "+uparts[i]).val()
	}
    }
    $("#graph .permalink").html(purl);
    if(copyme)
	copym($("#graph .permalink")[0],true);
    else
	return purl;
}
function finish_permalink(plparts,pchildren) {
    if(pchildren && pchildren.length > 0) {
	var index = pchildren[0]['index']
	current_score.splice(index,0,...pchildren.map(x => {
	    var y = {};
	    y[x.childlabel] = x.childval;
	    return y;
	}));
    }
    var ptranslate = "translate(120,-250)"
    if(window.innerWidth <= 1000)
	ptranslate = "translate(30,-90) scale(0.4,0.4)"
    d3.select("#pgroup").transition()
	.duration(600).attr("transform", ptranslate)
    setTimeout(function() {
	export_show(true)
	if(plparts[0])
	    $('#graph .ssvcvector').html(plparts[0]);
	if(plparts[1])
	    $('#graph .exportId').val(plparts[1])
	if(plparts[2])
	    $('#graph .exportRole').val(plparts[2]);
	$('#biscuit').fadeOut()
    }, 800)
}
function permalink() {
    if(location.hash == "")
	return;
    try {
	var plink = location.hash.substr(1);
	var pchildren = [];
	var plparts = plink.split("&");
	var fm = plparts[0].split("/");
	if(fm.length < 3) {
	    console.log("Location hash has no valid preload paramenters");
	    return;
	}
	topalert("Now loading permalink URL parameters","success");
	dt_clear();
	dt_start();
	$('#biscuit').fadeIn();	    
	$(".complex").attr("data-override",1);
	/* "SSVCv2/E:A/V:S/T:T/M:H/D:C/1632171335/&CVE-2014-01-01&Coordinator"
	   OR 
	   "SSVCv2/E:A/V:S/T:T/M:H/D:C/2021-01-09/&CVE-2014-01-01&Coordinator" */	
	var sI = {}
	var last_precheck = ""
	for(var i=1;i<fm.length-2;i++) {
	    var dtup = fm[i].split(":");
	    var fstep = export_schema.decision_points.filter(x => x.key == dtup[0]);
	    if(fstep.length != 1) {
		console.log("This decision point does not exist");
		console.log(dtup);
		continue;
	    }
	    var fopt = fstep[0].options.filter(x => x.key == dtup[1]);
	    if(fstep[0].label in ischild) {
		console.log("This is a child decision, do it later");
		pchildren.push({
		    index: i-1,
		    childlabel: fstep[0].label,
		    childval: fopt[0].label
		});
		continue;
	    }
	    var precheck = fopt[0].label.toLowerCase();
	    sI[precheck] = setInterval(
		function(u) {
		    if($('.prechk-'+u).length == 1) {
			$('.prechk-'+u).simClick();
			clearInterval(sI[u]);
			delete sI[u];
			if(u == last_precheck)
			    finish_permalink(plparts,pchildren);
			return;
		    }
		},600*i,precheck);
	    last_precheck = precheck;
	}
	setTimeout(function() {
	    for (let k in sI) {
		console.log("Pending jobs incomplete after 20 seconds");
		clearInterval(sI[k]);
		delete sI[k];
	    }
	},20000)
	console.log(sI);
    }catch(err) {
	console.log(err);
	topalert("Failed to parse Permalink URL!","error")
    }

}
function process(w) {
    var cve = $(w).val()
    if(cve == "import") {
	if(navigator.userAgent.indexOf("Chrome") < 0) {
	    $('#cvetsvload').show()
	    topalert("Choose the file to upload below")
	} else 
	    $('#cvetsvload').click()
	return
    }
    var cve_data = $('#'+cve).data()
    if(!cve_data) {
	alert("Some error in loading this CVE data check the template and try again")
	return
    }
    dt_clear();
    $('#biscuit').fadeIn();
    dt_start();
    
    $('#cve_table tbody tr td').remove()
    var steps = ['Exploit','Virulence','Technical']
    var stimes = [1600,3200,5100]
    //console.log(new Date().getTime())    
    for(var i=0; i< steps.length; i++) {
	clickprocess(steps[i],cve_data,stimes[i])
    }
    $('#biscuit').fadeOut(4930)
    for(var k in cve_data)
	$('#cve_table tbody tr').append("<td class='d-temp'>"+cve_data[k]+"</td>")
    $('#table_toggle').show()
}
function clickprocess(tstep,cve_data,stime) {
    setTimeout(function() {
	//console.log(tstep)
	//console.log(stime)
	//console.log(new Date().getTime())
	if(tstep in cve_data) {
	    if($(".prechk-"+cve_data[tstep].toLowerCase()).length == 1) {
		$(".prechk-"+cve_data[tstep].toLowerCase()).simClick()
	    } else {
		console.log("Try again in a few seconds "+tstep)
		//clickprocess(tstep,cve_data,stime-1000)
	    }
	} else {
	    console.log("Some strange error "+tstep)
	    console.log(cve_data)
	}
    },stime)
}

function load_tsv_score() {
    $.get("sample-ssvc.txt",tsv_load);
}
function tsv_load(data) {
    var rmv = $('#cve_samples option:nth-child(n+3)').remove().length
    $('#cve_table thead tr th').remove()
    var y = data.split("\n")
    var heads = y.shift().split("\t")
    var scores = y.map(x => { return x
			      .split("\t")
			      .reduce((map,obj,i) => {
				  map[heads[i]] = obj; return map;
			      },{}) })
	.filter(x => 'CVE' in x && x.CVE.length > 3)
	.sort(function(a, b) { if(a.CVE < b.CVE) return -1; else return 1})
    for(var i=0; i<scores.length;i++) {
	if(!('CVE' in scores[i])) continue
	$('#cve_samples').append($("<option></option>")
				 .attr("id",scores[i].CVE)
				 .text(scores[i].CVE)
				 .data(scores[i]))
    }
    $('#cve_samples').removeClass("d-none").addClass("form-control cve_samples")
    for(var i=0; i<heads.length;i++)
	$('#cve_table thead tr').append("<th>"+heads[i]
					.replace(/(\([^)]+\))/,
						 '<br><span class="text-muted">$1</span>')+
					"</th>")
    if(rmv) 
	topalert("Loaded TSV CVE samples count of "+scores.length,"success")
}
function create_short_keys(x,uniq_keys) {
    /* If a key is provided for short_key representation use it 
       if not detect one using the last */
    if("key" in x) {
	ssvc_short_keys[x.label] = x.key
	return true;
    }
    else {
	var iuniq = 0
	ssvc_short_keys[x.label] = x.label[0].toUpperCase()
	while (x.label[iuniq] in uniq_keys) {
	    iuniq = iuniq + 1;
	    ssvc_short_keys[x.label] = x.label[iuniq].toUpperCase()
	}
	uniq_keys[x.label[iuniq]] = 1;
	/* Create a key if one does not exist for reference in the full
	   exported JSON */
	x["key"] = ssvc_short_keys[x.label];
    }
}
function parse_json(xraw,paused) {
    var zraw = [];
    isparent = {};
    var tm;
    if(typeof(xraw) == "string") 
	tm = JSON.parse(xraw)
    else
	tm = xraw
    if('decision_tree' in tm) {
	/* This has a decision_tree and a score - a computed and provision
	   schemas together*/
	tm = tm.decision_tree;
    }
    /* Clear also non grphic trees */
    $('#ughtr').html('');
    $('#ugbtr').html('');
    $('.trcomplex').remove();
    if(!('decision_points' in tm)) {
	topalert("JSON schema has no decision_points","danger")
	return
    }
    if(!('decisions_table' in tm)) {
	topalert("JSON schema has no decision table, we can't help you with that","danger");
	console.log(tm);
	return;
    }
    /* Save JSON for export*/
    export_schema = tm
    /* This is temp key to find full child elements */
    var xkeys = {};
    /* Find array that are children as children will also have the decision 
       type simple */
    ischild = tm.decision_points.reduce(
	(x,y) => {
	    /* Use either key or label to create a hash of everyone */
	    xkeys[y.label] = y;
	    if("key" in y)
		xkeys[y.key] = y.label
	    /* Use either key or label to mark the xkeys to a child
	       decision tree */	    
	    if("children" in y) {
		console.log("Children for "+y.label);
		isparent[y.label] = [];
		y.children.map(z => {
		    var tx = z.label;
		    if(("key" in z) && (z.key != "")) {
			tx = xkeys[z.key];
		    }
		    isparent[y.label].push(xkeys[tx]);
		    x[tx] = 1;
		});
	    }
	    return x;
	},{});
    /* Check to make sure neither key nor label is in a ischild object */
    var x = tm.decision_points.filter(
	x => (!(x.label in ischild))).map(r => r.label)
    var y = tm.decisions_table
    //console.log(y)
    var yraw = [...Array(x.length)].map(u => [])
    var id = 1
    var thash = {}
    var decisions = tm.decision_points.filter(x => x.decision_type == "final")
    if('title' in tm)
	$('.cover_heading_append').html('('+tm.title+')');
    if(decisions.length != 1) {
	topalert("JSON schema has no decisions marked as final, assuming the last element is the \"Final\" decision.","warning")
	tm.decision_points[tm.decision_points.length - 1]['decision_type'] = "final"
	decisions = [tm.decision_points[tm.decision_points.length - 1]]
    }    
    final_keyword = decisions[0].label
    //console.log(decisions)
    //console.log(final_keyword)
    for(var i=0; i<y.length; i++) {
	//var tname = y[i].pop()+":"+y[i].join(":")
	//console.log(y[i])
	/* Decision table should have the "outcome" or "decision" fiel if not skip 
	   this entry */
	if(!(final_keyword in y[i]))
	    continue
	var tname = y[i][final_keyword]+":"+x.map(t => y[i][t]).slice(0,-1).join(":")
	for( var j=0; j< x.length-1; j++) {
	    //var tparent = x[x.length-2-j]+":"+y[i].slice(0,x.length-2-j).join(":")
	    var tparent = x[x.length-2-j]+":"+x.slice(0,x.length-2-j).map(q => y[i][q]).join(":")
	    //var tparent = x[x.length-1-j]+":"+x.slice(0,x.length-1-j).map(q => y[i][q]).join(":")
	    if(!(tname in thash))
		var yt = {name:tname.replace(/\:+$/,''),id:id++,parent:tparent.replace(/\:+$/,''),props:"{}",children:[]}
	    else
		continue
	    thash[yt.name] = 1
	    tname = tparent
	    yraw[j].push(yt)	    
	}
    }
    
    for(var j=yraw.length; j> -1; j--)  {
	if(yraw.length > 0)
	    zraw = zraw.concat(yraw[j])
    }

    /* Top or the first part of the tree data  */
    zraw[0] = {name:x[0],id:id+254,children:[],parent:null,props:"{}"}
    /* yraw[0].push({name:"Exploitation:",id:1024,children:[],parent:null,props:"{}"}) */
    raw = zraw
    //console.log(raw)
    topalert("Decision tree JSON has been updated with "+raw.length+
	     " nodes, with "+y.length+" possible outcomes, You can "+
	     "use it now!","success")
    dt_clear()
    /* Create label fields if they exists*/
    var lastdiv = "";
    /* Unique keys for decision points*/
    var duniq_keys = {};
    /* unique keys for choices under decision points*/
    var ouniq_keys = {};
    acolors = [];
    lcolors = {};    
    tm.decision_points.map(x => {
	create_short_keys(x,duniq_keys);
	var options_data = {}
	var options_html = x.options.reduce((h,r) => {
	    create_short_keys(r,ouniq_keys);
	    options_data[r.label] = r.description;
	    var rlabel = r.label[0].toLocaleUpperCase()+r.label.substr(1);
	    var spclass = 'popup-'+safedivname(r.label);
	    var div_add = "<div class='popupidiv "+spclass+"'><b>"+rlabel+"</b>&nbsp;"+r.description+"<hr /></div>";
	    return  h + div_add;
	},"<h5>"+x.label+"</h5>")
	var hdiv = safedivname(x.label)
	if($("."+hdiv).length != 1) {
	    //console.log(hdiv,"new");	    
	    $("."+hdiv).remove();
	    $('body').append($('<div/>').addClass("d-none "+hdiv));
	}
	$("."+hdiv).html(options_html)
	if(x.label in isparent) {
	    /* Save the entier decision object in data parent value*/
	    var mwbid = "mwb-"+hdiv;
	    $('body').append($('#mwb').clone().attr('id',mwbid));
	    var pmwbid = '#'+mwbid;
	    $(pmwbid).attr("data-parent",JSON.stringify(x));
	    $("."+hdiv+" h5").after("<p>(Complex Decision)</p>");
	    //console.log(isparent[x.label]);
	    $(pmwbid+" h5").html(x.label + " (Cummulative Score)");
	    //('#wbtable tr')
	    $(pmwbid+" .wbtable tr").remove();
	    isparent[x.label].forEach( (t,k) => {
		var stdiv = safedivname(t.label);
		var tselect = $("<select/>").addClass("form-control s-"+stdiv).
		    attr("data-moptions",JSON.stringify(t));
		t.options.forEach((v,l) => {
		    tselect.append($("<option/>").attr({
			"value":v.label}).text(v.label));
		});
		var tlabel = $("<span>").html(t.label+" ")
		    .append($("<a/>").attr({
			"class": "circletext",
			"onmouseover": "shwhelp(this)",
			"onmouseout": "hidediv(this)",
			"data-tdiv": stdiv,
			"href": "javascript:void(0)"
		    }).html("?"))
		var tr = $("<tr/>").append($("<td/>").append(tlabel)).
		    append($("<td/>").append(tselect));
		$(pmwbid+' .wbtable').append(tr);
		var addcontent = "<blockquote>Depends on "+String(k+1)
		addcontent += $("."+stdiv).html()+"</blockquote>";
		$('.'+hdiv).append(addcontent);
		$(pmwbid+' .btn-primary').removeAttr('onclick')
		    .attr({ 'data-tid': mwbid,'onclick': 'dynamic_mwb(this)'});
	    });
	}
	lastdiv = hdiv
	//console.log(options_data);
	$("."+hdiv).attr("data-options",JSON.stringify(options_data));	
    });
    $("."+lastdiv).addClass("Decision");
    var classes = []
    var decision_div = decisions[0].options.reduce((h,r,ir) => {
	classes.push(safedivname(r.label));
	if(("color" in r) && (r.color)) {
	    lcolors[r.label] = r.color;
	} else if(acolors[i]) {
	    r.color = acolors[i];
	}
	return h + $("<div>").append($("<strong/>").addClass("decisiontab").
				     css({color:r.color}).html(r.label))
	    .append("&nbsp"+r.description+"<hr>").html();
    },"<h5>"+final_keyword+"</h5>")
    if($("."+classes[0]).length != 1) {
	$("."+classes[0]).remove()
	$('body').append($('<div/>').addClass("d-none "+classes[0]))
    }
    //console.log(classes)
    //console.log(decision_div)
    $("."+classes[0]).addClass(classes.join(" ")).html(decision_div)
    permalink();
    $('#dtreecsvload').hide();
}
function shwhelp(w) {
    var iconPos = w.getBoundingClientRect();
    var tm = $(w).data('tdiv')
    if(tm) {
	$('#mpopup').css({left:(iconPos.right + 10) + "px",
			  top:(window.scrollY + iconPos.top - 20) + "px",
			  "max-width": "-moz-available",
			  "max-width": "-webkit-fill-available",
			  "max-width": "stretch",
			  "overflow-y": "auto",
			  "z-index":1050,
			  display:"block"});
	$('#mpopup').html($('.'+tm).html())
	$('.complex').on('hidden.bs.modal', function (e) {
	    $('#mpopup').hide();
	})
    }
    $('#mpopup').show()
}


function safedivname(instr) {
    var uri_esc = encodeURIComponent(instr)
    var safestr = btoa(uri_esc.replace(/%([0-9A-F]{2})/g,
				       (m, p)  =>
				       String.fromCharCode('0x' + p)));
    var fstr = "d-"+safestr.replace(/[\+\/\=]/gi,
				    (m,p) => { return m.charCodeAt(0) });
    return fstr.substr(0,14);
}


function create_export_schema_dtable(yi,x) {
    export_schema.decisions_table.push(yi.reduce((a,b,c) => {
	/* Add labels that do not exist */
	if(export_schema.decision_points[c]['options']
	   .filter(d => ('label' in d) && (d.label == b)).length != 1)
	    export_schema.decision_points[c]['options'].push({label: b, description:b})
	a[x[c]] = b
	return a; },{}))
}
function parse_file(xraw) {
    /* This is really parse csv instead of parse JSON */
    //var xraw = 'TSV data'
    var zraw=[]
    export_schema.decision_points =  []
    export_schema.decisions_table =  []
    /* CSV or TSV looks like 
       ID,Exploitation,Utility,TechnicalImpact,SafetyImpact,Outcome
    */
    var xarray = xraw.split('\n')
    var xr = xarray.map(x => x.split(/[\t,]+/))
    /* Remove first row has the headers and pass the rest to variable y */
    var y = xr.splice(1)
    /* Check if rowID first column of second row to match not number*/
    var is_ssvc_v1 = y[0][0].match(/\D+/) ? false : true
    /* Remove ID column in the first row to create x*/
    if (is_ssvc_v1) 
	var x = xr[0].splice(1)
    else
	var x = xr[0]
    /* Now xr looks like below for ssvc csv v1 */
    /* [["Row", "Exploitation", "Virulence", "Technical", "Mission_Well-being", "Decision"]] */
    //var yraw = [[],[],[],[],[]]
    /* Register the export schema decision points, assume all decisions are simple */
    export_schema.decision_points = x.map(
	dc => {
	    var ix = {decision_type:"simple", options:[]}
	    ix.label =  dc
	    return ix
	})
    /* make the last column final decision/outcome/action */
    export_schema.decision_points[export_schema.decision_points.length-1].decision_type="final"
    /* Initialize Empty arrray */
    var yraw = [...Array(x.length)].map(u => []);
    var id=1;
    /* This will create just the last branches of the tree */
    var thash = {}
    for(var i=0; i< y.length - 1; i++) {
	if(y[i].length < 1) continue
	/* Remove ID column if it is SSVC v1*/
	if(is_ssvc_v1)
	    y[i].shift()
	/* Add lame CSV/TSV data to export schema */
	//console.log(y[i]);
	create_export_schema_dtable(y[i],x)
	var tname = y[i].pop()+":"+y[i].join(":")
	//console.log(tname)
	if(tname == "undefined") continue;
	for( var j=0; j< x.length-1; j++) {
	    /*y[i] look like 0,none,laborious,partial,none,defer */
	    var tparent = x[x.length-2-j]+":"+y[i].slice(0,x.length-2-j).join(":")
	    //console.log(tparent)
	    if(!(tname in thash))
		var yt = {name:tname.replace(/\:+$/,''),id:id++,parent:tparent.replace(/\:+$/,''),props:"{}",children:[]}
	    else
		continue
	    thash[yt.name] = 1
	    tname = tparent
	    yraw[j].push(yt)
	}
    }
    /* This step below is not necessary now as the above routine goes from 
       0 -> y.length, instead  of 0 to y.length -1. 
       Remove ID column and Add the last row into export schema */
    //y[y.length-1].shift()
    //create_export_schema(y[y.length-1],x)
    for(var j=yraw.length; j> -1; j--)  {
	if(yraw.length > 0)
	    zraw = zraw.concat(yraw[j])
    }
    /* Next part of the tree data  */
    zraw[0] = {name:x[0],id:id+254,children:[],parent:null,props:"{}"}
    /* yraw[0].push({name:"Exploitation:",id:1024,children:[],parent:null,props:"{}"}) */
    raw = zraw
    var detect_version = "v2"
    if(is_ssvc_v1)
	detect_version = "v1"
    topalert("Decision tree has been updated with "+raw.length+" nodes, with "+
	     y.length+" possible decisions using "+detect_version+" CSV/TSV file, You can use it now!","success")
    dt_clear()
    export_schema.decision_points[export_schema.decision_points.length-1].
	options.map((x,i) => lcolors[x.label] = acolors[i] )
}

function add_invalid_feedback(xel,msg) {
    $('.invalid-feedback').remove()
    $('.valid-feedback').remove()    
    if(msg == "")
	msg = 'Please provide valid data for '+$(xel).attr('name')
    var err = $('<div>').html(msg)
    $(xel).after(err)
    $(err).addClass('invalid-feedback').show()
    $(xel).focus()
}
function add_valid_feedback(xel,msg) {
    $('.invalid-feedback').remove()
    $('.valid-feedback').remove()        
    if(msg == "")
	msg = 'Looks good'
    var gdg = $('<div>').html(msg)
    $(xel).after(gdg)
    $(gdg).addClass('valid-feedback').show()
}
function verify_inputs() {
    var inputs=$('#main_table :input').not('button')
    for (var i=0; i< inputs.length; i++) {
	if(!$(inputs[i]).val()) {
	    if(!$(inputs[i]).hasClass("not_required")) {
		add_invalid_feedback(inputs[i],"")
		return false
	    }
	}
    }
    return true
}
function generate_uuid() {
    var uuid = Math.random().toString(16).substr(2,8)
    for (var i=0; i<3; i++)
	uuid += '-'+Math.random().toString(16).substr(2,4)
    return uuid+'-'+Math.random().toString(16).substr(2,12)
}

function draw_graph() {
    var margin = {top: 20, right: 120, bottom: 20, left: 120},
	width = 1060 - margin.right - margin.left,
	height = 800 - margin.top - margin.bottom
    if(showFullTree) {
	var add_offset = 0
	if(raw.length > 60 )
	    add_offset = (raw.length - 60)*5
	//margin.left = margin.left + (raw.length - 60)*2
	//width = 1200 - margin.right - margin.left + add_offset*0.5
	height = 1300 - margin.top - margin.bottom + add_offset
    }
    duration = 750
    tree = d3.layout.tree()
	.size([height, width]);

    diagonal = d3.svg.diagonal()
	.projection(function(d) { return [d.y, d.x]; });

    //xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
    var default_translate =  "translate(" + margin.left + "," + margin.top + ")"
    var svg_width = width + margin.right + margin.left
    var svg_height = height + margin.top + margin.bottom
    if(window.innerWidth <= 1000) {
	default_translate =  "translate(10,0) scale(0.75)"
	if(window.innerWidth <= 750)
	    default_translate =  "translate(30,0) scale(0.42)"
    }
    $('#zoomcontrol').show();
    $('#zoomcontrol input').val(100);
    svg = d3.select("#graph").append("svg")
	.attr("xmlns","http://www.w3.org/2000/svg")
	.attr("preserveAspectRatio","none")
	.attr("class","mgraph")
	.attr("width", svg_width)
	.attr("height", svg_height)
	.append("g")
	.attr("transform", default_translate)
	.attr("id","pgroup")

    root = treeData[0];
    root.x0 = height / 2;
    root.y0 = 0;

    update(root)

    d3.select(self.frameElement).style("height", "700px");
    /*
      var svgx = $('svg')[0].outerHTML
      $('#dlsvg').attr('href','data:image/svg+xml;charset=utf-8,'+ encodeURIComponent(svgx))
      $('#dlsvg').attr('download','SVG-'+timefile()+'.svg')
    */
}
function check_children(d,a,b) {
    if((d.children) && (d.children.length)) return a
    if((d._children) && (d._children.length)) return a
    return b
}
function update(source) {
    var i = 0
    // Compute the new tree layout.
    var nodes = tree.nodes(root).reverse()
    var links = tree.links(nodes)

    // Normalize for fixed-depth.
    nodes.forEach(function(d) { d.y = d.depth * 200;})

    // Update the nodes…
    var node = svg.selectAll("g.node")
	.data(nodes, function(d) { return d.id || (d.id = ++i); });

    // Enter any new nodes at the parent's previous position.
    var nodeEnter = node.enter().append("g")
	.attr("class", "node bof")
	.attr("transform", function(d) {
	    return "translate(" + source.y0 + "," + source.x0 + ")";	    
	})
	.attr("class", function(d) {
	    if('depth' in d)
		return "node depth-"+String(d.depth);
	    return "node depth-none";})
	.on("click", doclick)
	.on("contextmenu",dorightclick)
	.on("mouseover",showdiv)
	.on("mouseout",hidediv);

    nodeEnter.append("circle")
	.attr("r", 1e-6)
	.attr("class","junction gvisible")
	.style("fill", function(d) {
	    if(d._children) return "lightsteelblue"
	    if(!('children' in d)) {
		/* Last node no children */
		var dname = d.name.split(":").shift();
		if(dname in lcolors) 
		    return undefined;

	    }
	    return undefined;
	}  );
    
    /*
      nodeEnter.append("text")
      .attr("x", function(d) { return check_children(d,"-13","-60")})
      .attr("y", "+10")
      .attr("dy", ".35em")
      .attr("class","dfork")
      .attr("text-anchor", function(d) { return check_children(d,"end","start") })
      .text( function(d) {
      if(d.name.split(":").length > 1) return d.name.split(":").pop();
      return "";
      })
      .style("fill-opacity", 1e-6)
      .style("font-size","14px")
      .style("fill","white")
    */
    var font = "20px"
    if(showFullTree) 
	font = "18px"
    nodeEnter.append("text")
	.attr("x",function(d) { return check_children(d,"-55","+20") })
	.attr("y",function(d) { return check_children(d,"-37","0") })
	.attr("dy", ".35em")
	.attr("class",function(d) {
	    return "gvisible prechk-"+d.name.split(":").shift().toLowerCase()
	}).text(function(d) { return d.name.split(":")[0]; })
	.style("font-size",font)
	.style("fill", function(d) {
	    var t = d.name.split(":").shift();
	    var x;
	    if(t in lcolors)
		x = lcolors[t];
	    return x;
	})

    /* hidden circle */
    nodeEnter.append("circle")
	.attr("r","10")
	.attr("class","ghidden d-none")
	.style("fill","steelblue");


    // Transition nodes to their new position.
    var nodeUpdate = node.transition()
	.duration(duration)
	.attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

    nodeUpdate.select("circle")
	.attr("r", 10)
	.attr("sid",function(d) { return d.id;})
	.attr("nameid",function(d) { if(!d) return "1";
				     if(d.name) return d.name.split(":").pop();
				   })
	.style("fill", function(d) {
	    if(d._children) return "lightsteelblue"
	    if(!('children' in d)) {
		var dname = d.name.split(":").shift()
		if(dname in lcolors) 
		    return lcolors[dname];
	    }
	    return undefined;
	})
	.style("stroke",function(d) {
	    if(!('children' in d)) {
		var dname = d.name.split(":").shift()
		if(dname in lcolors) 
		    return undefined;
	    }	    
	    return "steelblue";
	})


    nodeUpdate.select("text")
	.style("fill-opacity", 1);

    // Transition exiting nodes to the parent's new position.
    var nodeExit = node.exit().transition()
	.duration(duration)
	.attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
	.remove();

    nodeExit.select("circle")
	.attr("r", 1e-6);

    nodeExit.select("text")
	.style("fill-opacity", 1e-6);

    // Update the links…

    var link = svg.selectAll("path.link")
	.data(links, function(d) { if(d.target) return d.target.id; })
    /*        .enter()
              .append("g")
              .attr("class", "link")
    */
    // Enter any new links at the parent's previous position.
    //var linkx = link.enter().append("g").attr("class","pathlink").attr("d","")
    //linkx.append("path")
    link.enter().insert("path","g")
	.attr("class", "link")
	.attr("id", function(d) { return 'l'+Math.random().toString(36).substr(3); })
	.attr("kdata", function(d) { return d.source.name.split(":").shift(); })
	.attr("ldata", function(d) { return d.target.name.split(":").pop(); })
	.attr("ldeep", function (d) { return d.target.name.split(":").length })
	.attr("csid",function(d) { return d.target.id;})    
	.attr("d", function(d) {
	    var o = {x: source.x0, y: source.y0};
	    return diagonal({source: o, target: o});
	})

    // Transition links to their new position.
    link.transition()
	.duration(duration)
	.attr("d", diagonal);

    // Transition exiting nodes to the parent's new position.
    link.exit().transition()
	.duration(duration)
	.attr("d", function(d) {
	    var o = {x: source.x, y: source.y};
	    return diagonal({source: o, target: o});
	})
	.remove();

    // Stash the old positions for transition.
    nodes.forEach(function(d) {
	d.x0 = d.x;
	d.y0 = d.y;
    });
    if(showFullTree === false) {
	var d = source;
	if(('depth' in d) && (!isNaN(parseInt(d.depth)))) {
	    $('g.depth-'+String(d.depth)+' .ghidden').addClass('d-none');
	    $('g.depth-'+String(d.depth)+' .gvisible').show();
	    $('g.depth-'+String(d.depth)).removeClass('opthide');
	    var idepth = String(parseInt(d.depth) + 1)
	    if($('g.depth-'+idepth).length > 0) {
		$('g.depth-'+idepth+' .ghidden').removeClass('d-none');
		$('g.depth-'+idepth+' .gvisible').hide();
		$('g.depth-'+idepth).addClass('opthide');
	    }
	}
    }
    setTimeout(update_links,1500);
}
function pathclick(w) {
    var sid = $(this).attr("csid")
    if(sid) {
	$('circle[sid="'+sid+'"]').parent().simClick()
    }
}
function update_links() {
    /* d3.select("g").append("g").attr("class","pathlink").append("path").attr("d","M0,480C90,480 90,800 180,800").attr("class","link")
       <path class="link" id="mo7ejxrk19" ldata="low" d="M540,920C630,920 630,900 720,900"></path>
    */
    $('.pathlink').remove()
    var i = 0
    d3.selectAll("path.link").each(function(w) {
	var t = $(this);
	var id=t.attr("id");
	var xd = t.attr("d")
	var csid = t.attr("csid")
	var depth = parseInt(t.attr("ldeep")) || 0
	var text = t.attr("ldata")
	var pname = t.attr("kdata")
	var xclass = "btext prechk-"+text
	var mclass = $(this).attr("class")
	if((mclass) && mclass.indexOf("chosen") > -1) {
	    xclass += " chosen"
	}
	if(showFullTree)
	    xclass += " fullTree"
	d3.select("g")
	    .insert("g","path.link").attr("class","pathlink cdepth-"+String(depth)).attr("id","x"+id)
	    .append("path").attr("d",xd).attr("id","f"+id).attr("class","xlink")
	// depth 4 => 70 , depth 0 => 40%
	var doffset = parseInt(70 - (4-depth)*5.5)
	var yoffset = -10
	if(showFullTree)
	    yoffset = -6
	d3.select("g#x"+id).append("text").attr("dx",-6).attr("dy",yoffset).attr("class","gtext")
	    .append("textPath").attr("href","#f"+id).attr("class",xclass)
	    .attr("id","t"+id)
	    .attr("csid",csid)
	    .attr("parentname",pname)
	    .text(text).attr("startOffset",doffset+"%")
	    .on("click",pathclick)
	    .on("mouseover",showdiv)
	    .on("mouseout",hidediv);
	//.each(function() { console.log("Completed") })
	//$(this).remove() "fill","#17a2b8") "text-anchor","middle"
    })
}
function showdiv(d) {
    var iconPos = this.getBoundingClientRect();
    //console.log(JSON.parse(d.props))
    var bgcolor = 'rgba(70, 130, 180, 1)';
    var name = "";
    var highlighter = "";
    if($(this).is('g'))
	name = $(this).find("text").text();
    else if($(this).is('circle')) 
	name = $(this).parent().find("text").text();
    else if($(this).is('textPath')) {
	name = $(this).attr("parentname");
	highlighter = $(this).text();
    }
    if($(this).hasClass('opthide')) {
	/* find depth-n*/
	var idepth = Array.from(this.classList).find(a => a.indexOf("depth") == 0).replace("depth-","");
	//console.log(idepth);
	var intdepth = parseInt(idepth);
	if(intdepth > 0) {
	    var pdepth = intdepth - 1;
	    var pgitem = $('g.depth-'+String(pdepth));
	    if(pgitem.length > 0) {
		name = pgitem.find("text").text()
		var csid = $(this).find("circle.junction").attr("sid");
		var gtext = $('textPath[csid="'+csid+'"]')
		if(gtext.length > 0) {
		    highlighter = gtext.text();
		}
		
	    }
	}
	
    }
    //name=name.replace(/\W/g,'_')
    //console.log(name)
    //console.log(vul_data)
    var addons = ''
    var safename = safedivname(name)
    //console.log(name,safename)
    /* Default left position*/
    var leftpos = String(iconPos.right + 10) + "px"
    if(window.innerWidth - iconPos.right < iconPos.right) {
	/* right half of screen, move left position */
	leftpos = String(iconPos.left - $('#mpopup').width()) +"px"
    }
    
    if($('.'+safename).length == 1) {
	$('#mpopup').html($('.'+safename).html())
	$('#mpopup').css({left: leftpos,
			  top:(window.scrollY + iconPos.top - 20) + "px",
			  display:"block"});
    }
    if(highlighter != "") {
	$('#mpopup .popupidiv').addClass('not-highlighted').removeClass('highlighted');
	var spclass = 'popup-'+safedivname(highlighter);
	$('#mpopup .'+spclass).addClass('highlighted');
    } else {
	$('#mpopup .popupidiv').removeClass('not-highlighted highlighted');
    }
}
function hidediv(d) {
    $('#mpopup').hide()
}
function checkclose() {
    /* */
    $('#mpopup').hide();
}
function tmp_dismiss_modal() {
    $('.complex').modal('hide');
    $('#tcummulative').removeClass('d-none');
    setTimeout(function() {
	$('#tcummulative').addClass('d-none');
    },3000);
    
}


function dorightclick(d) {
    return
}
function closeSiblings(d) {
    d.clickkill = true
    if (!d.parent) return; // root case
    /* 

     */
    var x = d.parent.children
    d.parent._children = d.parent.children
    d.parent.children = [d]
    //console.log(d.parent)
}
function revert(d) {
    var save_score = current_score.splice(0,d.depth);
    dt_clear();
    dt_start();
    var sI = {};
    for(var i=0; i< save_score.length; i++) {
	var nodename = Object.keys(save_score[i]).shift()
	var nodevalue = save_score[i][nodename];
	sI[nodename] = setInterval(
	    function(n,v) {
		/* $('[parentname="Exploitation"].prechk-none').simClick() */
		var selector = '[parentname="'+n+'"].prechk-'+v
		if($(selector).length == 1) {
		    $(selector).simClick();
		    clearInterval(sI[n]);
		    delete sI[n];
		    console.log("Cleared");
		    console.log(n,v);
		    console.log(sI);
		    return;
		} else {
		    console.log("Waiting");
		    console.log(n,v);
		}
	    },600*i,nodename,nodevalue);
    }
    console.log(d);
}
function doclick(d) {
    if(showFullTree === false) {
	hidediv();
	if(('clickkill' in d) &&
	   (d.clickkill === true)) {
	    if(('depth' in d) && (d.depth < current_score.length)) {
		var nodename = d.name.split(":").shift();
		if(confirm("Are you sure you want to revert the decision to Node: "+nodename+"?")) {
		    revert(d);
		    return;
		}
	    }
	    
	    console.log("We have reached this already ");
	    console.log(d);
	    return;
	} 
	if(d.parent && d.parent.name) {
	    /* Virulence:none means Exploitation(i.e., d.parent.name) => none*/
	    var dparent = d.parent.name.split(":").shift();
	    var thash = {};
	    thash[dparent] = d.name.split(":").pop();
	    current_score.push(thash);
	}
	$('.pathlink').remove();
	if('name' in d) {
	    var dnames = d.name.split(":");
	    var leftname = dnames.shift();
	    var rightname = dnames.pop();
	    if($('circle[nameid="'+rightname+'"]').length == 1) {
		if($('circle[nameid="'+rightname+'"]').attr("isfinal") == "1")
		    export_show();
	    }
	    if(leftname in isparent) {
		/* If mwb is overriden by permalink or full score reset 
		   it and ignore it*/
		console.log(leftname);
		if($(".complex").data("override") == 1) 
		    $(".complex").attr("data-override",0)
		else
		    $('#mwb-'+safedivname(leftname)).modal()
	    }
	}
	if('id' in d) {
	    var idl = $('[csid="'+d.id+'"]').attr("id")
	    d3.select('#f'+idl).attr('class','chosen link')
	    d3.select('#t'+idl).attr('class','chosen btext')		
	    d3.select('#'+idl).attr('class','chosen link')
	}
	if(d.parent) 
	    closeSiblings(d);
	if(('_children' in d) && (d._children.length == 0))
	    export_show();
    }
    $('.pathlink').remove()    
    if (d.children) {
	d._children = d.children;
	d.children = null;
    } else {
	d.children = d._children;
	d._children = null;
    }
    update(d);
}

function grapharray(array){
    var map = {};
    for(var i = 0; i < array.length; i++){
	var obj = array[i];
	obj._children= [];

	map[obj.name] = obj;

	var parent = obj.parent || '-';
	if(!map[parent]){
	    map[parent] = {
		_children: []
	    };
	}
	map[parent]._children.push(obj);
    }
    return map['-']._children;
}

function grapharray_open(marray){
    var map = {};
    for(var i = 0; i < marray.length; i++){
	var obj = marray[i];
	obj.children= [];

	map[obj.name] = obj;

	var parent = obj.parent || '-';
	if(!map[parent]){
	    map[parent] = {
		children: []
	    };
	}
	map[parent].children.push(obj);
    }
    return map['-'].children;
}

function timefile() {
    var d = new Date();
    return d.getDate()  + "-" + (d.getMonth()+1) + "-" + d.getFullYear() + "-" +
	d.getHours() + "-" + d.getMinutes()
    
}
function showme(divid,vul_flag) {
    $('.scontent').hide()
    $(divid).show()
    if(vul_flag)
	$('#vuls').removeClass('d-none')
    else
	$('#vuls').addClass('d-none')
}

function dt_start() {
    current_score = [];
    showFullTree = false
    $('svg.mgraph').remove();
    $('#graph .exportdiv').remove();
    var xraw = JSON.parse(JSON.stringify(raw));
    treeData=grapharray(xraw);
    draw_graph();
    /* reset all Complex decision select boxes*/
    $('.complex select').each(function(_,x) { console.log(x.selectedIndex = 0)});    
    setTimeout(function() {
	$('circle.junction').parent().simClick()
	/* Disable click on the first node */
	treeData[0].clickkill = true
    }, 900)
}
function dt_clear() {
    showFullTree = false;
    current_score = [];
    raw.map(x => {  x.children=[]; delete x._children;});
    /* Clear all graph to start */
    $('svg.mgraph').remove();
    $('#graph').html('');
}

function show_full_tree() {
    showFullTree = true
    $('#graph .exportdiv').remove()
    $('svg.mgraph').remove()
    var xraw = JSON.parse(JSON.stringify(raw))
    treeData=grapharray_open(xraw)
    draw_graph()
}


function add_text(links) {
    var link = svg.selectAll(".link")
	.data(links)
	.enter()
	.append("g")
	.attr("class", "link");

    link.append("path")
	.attr("fill", "none")
	.attr("stroke", "#ff8888")
	.attr("stroke-width", "1.5px")
	.attr("d", diagonal);

    link.append("text")
	.attr("font-family", "Arial, Helvetica, sans-serif")
	.attr("fill", "Black")
	.style("font", "normal 12px Arial")
	.attr("transform", function(d) {
	    return "translate(" +
		((d.source.y + d.target.y)/2) + "," +
		((d.source.x + d.target.x)/2) + ")";
	})
	.attr("class",function(d) { return d.target.name.toLowerCase(); })
	.attr("dy", ".35em")
	.attr("text-anchor", "middle")
	.text(function(d) {
	    //console.log(d.target.name);
	    return d.target.name;
	});
}
function createHeaders(keys) {
    var result = [];
    for (var i = 0; i < keys.length; i += 1) {
	result.push({
	    id: keys[i],
	    name: keys[i],
	    prompt: keys[i],
	    width: 65,
	    align: "center",
	    padding: 0
	});
    }
    return result;
}
function deepsearch(obj,dir) {
    var xobj = obj
    var path = dir.split(".")
    for(var i=0; i<path.length; i++) {
	if(path[i] in xobj)
	    xobj = xobj[path[i]]
	else
	    return null
    }
    return xobj
}

function export_pdf() {
    $('.Exporter').css({'pointer-events':'none'})
    var vul = $('#graph .exportId').val().toUpperCase();
    if((vul == "") || (vul.indexOf("CVE") < 0)) {
	createPDF(vul,"No further information available");
	console.log("No vul information such as CVE");
	return;
    }
    var cve_json_url = "https://olbat.github.io/nvdcve/";
    $.getJSON(cve_json_url+vul+".json").done(function(d) {
	var f = deepsearch(d,"cve.description.description_data.0.value");
	if((!f) || (f == ""))
	    f = "No further information available"
	createPDF(vul,f);
    }).fail(function() {
	console.log("No CVE information available");
	console.log(arguments);
	$('.Exporter').css({'pointer-events':'all'});
    })


}
function createPDF(vulnerability,cveinfo) {
    //    Requirements for new updates for the ssvc-calc tool.
    var role = $('#graph .exportRole').val() || "Unknown";
    var vulid = $('#graph .exportId').val() || "Unspecified";
    var includetree = $('#graph .includetree').is(':checked');        
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF({putOnlyUsedFonts:true});
    var coord = $('.cover_heading_append').html().replace(/^\s+(.+)\s+/g,'$1')
    var vulnerability = $('#graph .exportId').val();
    if(vulnerability == "")
	vulnerability = "ID-Pending"
    var title = "SSVC score for "+vulnerability+" "+coord
    doc.setFont("helvetica", "bold");
    var q = doc.getStringUnitWidth(title)
    doc.text(title, 100-q*2.5, 10);
    var steps = current_score.map(x => Object.keys(x)[0]);
    var decisions = current_score.map((x,i) => x[steps[i]]);
    final_outcome =  $('#graph svg g.node text:last').text();
    decisions.push(final_outcome);
    /* Removing hard-coded "Decision" field so it is flexible*/
    steps.push(final_keyword);
    /* var steps=["Exploitation","Virulence","Technical Impact","Mission & Well-Being","Decision"] */
    /* var decisions = ["Active","Slow","Partial","Low","Track"] */
    var actions = []
    var xOffset = 20
    var yOffset = 30
    var cradius = 3
    var ysteps = 40

    /* fill: rgb(176, 196, 222);
       stroke: rgb(70, 130, 180);*/ 
    var ij = 0;
    for (var i=0; i< steps.length; i++) {
	if(steps[i] in ischild) {
	    console.log("Skipping this one as it is a child decision");
	    console.log(steps[i]);
	    continue;
	}
	var x = xOffset+ysteps*ij;
	doc.setLineWidth(1);
	doc.setFont("helvetica",'bold');
	doc.setDrawColor(70,130,180);
	doc.setFillColor(176, 196, 222);
	if(i == steps.length - 1) {
	    /* Last circle change color */
	    if(final_outcome in lcolors) {
		doc.setDrawColor(192,192,192);
		doc.setFillColor(lcolors[final_outcome]);
	    }
	    
	}
	doc.circle(x, yOffset, cradius, "FD");
        q = doc.getStringUnitWidth(steps[i])
	//#343a40
	doc.setTextColor(0x11,0x3a,0x40);
	doc.setFontSize(12);
	//doc.setFont(undefined,'bold')
	doc.text(steps[i],x-q*2,yOffset-5);
	if (i < steps.length-1) {
	    /* Not Final decision */
	    doc.line(x+3,yOffset,x+3+34,yOffset)
	    //#17a2b8 !important
	    doc.setTextColor(0x17,0xa2,0xb8);
	    doc.setFont("courier","bolditalic");
            doc.text(decisions[i],x+q*2,yOffset+4)
	}
	ij++;
    }

    //    rgb(40, 167, 69);
    doc.setFont("courier");
    //doc.setFontType("bolditalic");
    doc.setFont("courier",'bolditalic')
    var lastx = xOffset+ysteps*(ij-1)+10
    if(final_outcome in lcolors)
	doc.setTextColor(lcolors[final_outcome])
    else
	doc.setTextColor(1,1,1)
    doc.text(final_outcome,lastx,yOffset+1);
    
    doc.setFont("helvetica",'bold');
    doc.setTextColor(0,0,0);
    doc.setFontSize(14);
    xOffset = 12;
    doc.text("Summary",xOffset,yOffset+13);
    doc.setFontSize(12);
    var vector_string = $('#graph .ssvcvector').html()

    doc.setFont("helvetica","normal");
    doc.text("Recommendation:",xOffset,yOffset+20);    
    doc.text("SSVC Vector   :",xOffset,yOffset+25);
    doc.text("Timestamp:",xOffset,yOffset+30);
    doc.text("SSVC Role:",xOffset,yOffset+35);
    doc.text("Vulnerability Info:",xOffset,yOffset+40);

    doc.setFont("courier",'italic');
    var ycve = vulnerability.toUpperCase()
    if(ycve.indexOf("CVE") == 0) {
	var link = 'https://nvd.nist.gov/vuln/detail/'+ycve
	doc.setTextColor(0,0,255);
	doc.textWithLink(vulnerability, xOffset+40, yOffset+40, {url: link});
	doc.setLineWidth(0.5);
	doc.setDrawColor(0,0,255);
	doc.line(xOffset+40,yOffset+41,xOffset+40+33,yOffset+41)
	//doc.text(xOffset+40,yOffset+20,link);
	doc.setTextColor(0,0,0);
    } else {
	doc.text(vulnerability, xOffset+40, yOffset+40);
    }
    doc.text(vector_string,xOffset+40,yOffset+25);
    q = doc.getStringUnitWidth(vector_string)
    doc.addImage("icons8-copy-link-48-blue.png","PNG",60+q*4,yOffset+20,6,6);
    var purl = create_permalink(false);
    doc.link(61+q*4,yOffset+21,12,12,{url: purl});
    var timeprint = "";
    doc.setFont("courier",'italic');        
    if(vector_string.match(/\/[0-9]+\/$/)) {
	var ts = new Date(parseInt(vector_string.split('/').slice(-2,-1)[0]*1000));
	timeprint = ts.toGMTString().replace("GMT","UTC");
    } else {
	var tmsec = Date.parse(vector_string.split('/').slice(-2,-1)[0]);
	var ts = new Date(tmsec);
	timeprint = ts.toGMTString().replace("GMT","UTC");
    }
    doc.setFont("courier","bolditalic");    
    if(final_outcome in lcolors) {
	doc.setTextColor(lcolors[final_outcome]);
    }
    doc.text(final_outcome,xOffset+40,yOffset+20);
    doc.setTextColor(0,0,0);
    doc.setFont("courier",'italic');
    doc.text(timeprint,xOffset+40,yOffset+30);
    var role = coord;
    doc.text(role,xOffset+40,yOffset+35);
    var ynow = yOffset + 40
    if(cveinfo.length > 28) {
	/* Treat first line in a different way*/
	var ft = cveinfo.match(/.{1,27}(\s|$)/g);
	q = doc.getStringUnitWidth(vulnerability);	
	doc.text(ft[0],xOffset+40+q*4.4,ynow);
	ynow = ynow+5
	cveinfo = cveinfo.substr(ft[0].length);
	var f = cveinfo.match(/.{1,45}(\s|$)/g);
	for (var j = 0; j<f.length; j++) {
	    doc.text(f[j],xOffset+40,ynow);
	    ynow = ynow + 5
	}
    } else {
	ynow = ynow + 5
    }
    //doc.text(cveinfo,xOffset+40,yOffset+45);
    doc.setFont("helvetica",'bold');
    doc.setFontSize(14);
    doc.text("Details",xOffset,ynow);
    ynow = ynow + 7
    var t = []
    steps.forEach((x,i) => {
	var ix = $('.'+safedivname(x)).data('options');
	if(typeof(ix) != "object") return t.push("No information provided");
	else if(decisions[i] in ix) return t.push($("<div>").html(ix[decisions[i]]).text());
	return t.push("No information available")
    })
    doc.setFontSize(12);
    for(var i = 0; i < t.length; i++) {
	if(steps[i] in ischild) {
	    continue;
	}
	if(steps[i] in isparent) {
	    var q = isparent[steps[i]];
	    var istring = "This is a cummulative score of \"";
	    q.forEach(x => {
		if('label' in x) {
		    var t = current_score.forEach(
			(b) => {
			    if(x.label in b) {
				istring += x.label +"\" => \""+b[x.label]+"\" and "
			    }
			},"");
		    }
	    })
	    /* Replace the string with cummulative information */
	    t[i] = istring.slice(0,-5) + ".  Review the full SSVC tree for details."
	}
	doc.setFont("helvetica",'bold');
	doc.text(steps[i]+":",xOffset,ynow);
	q = doc.getStringUnitWidth(steps[i])
	
	doc.setTextColor(0x17,0xa2,0xb8);
	if(decisions[i] in lcolors)
	    doc.setTextColor(lcolors[decisions[i]]);
	doc.setFont("courier","bolditalic");
	doc.text(decisions[i],xOffset+q*4.8,ynow);
	doc.setTextColor(0,0,0);
	doc.setFont("courier",'normal');
	q = q + doc.getStringUnitWidth(decisions[i])

	var f = t[i].match(/.{1,45}(\s|$)/g);	
	doc.text("=> "+f[0],xOffset+q*5,ynow);
	if(t[i].length<= f[0].length) {
	    ynow = ynow +10
            continue
	}	
	//console.log(t[i].substr(f[0].length));
	f = t[i].substr(f[0].length).match(/.{1,65}(\s|$)/g);
	for (var j = 0; j<f.length; j++) {
	    doc.setFont("courier",'normal')
	    ynow = ynow +5
	    doc.text(f[j],xOffset,ynow);
	}
	ynow = ynow +10
    }
    doc.setFont("helvetica",'bold');
    doc.text("Contact:",xOffset,ynow);
    doc.setFont("courier",'normal');
    doc.text($('#contact').val(),xOffset+20,ynow);
    var safetime = ts.toGMTString().replace(/[^a-z0-9]+/ig,'-');
    var fulltree = includetree ? "-with-full-tree" : ""
    var dfilename = "SSVC-"+role+"-"+vulid+"-"+safetime+fulltree+".pdf";
    if(includetree)
	appendtree(doc,dfilename)
    else 
	doc.save(dfilename);
    $('.Exporter').css({'pointer-events':'all'});
}
function sigmoid(flen) {
    var lasty = flen*(1/(1+Math.exp(0.5*8)));
    var p =[]
    for(var i=-8;i<8;i=i+0.3) {
	y = flen*(1/(1+Math.exp(-0.5*i)))
	//console.log(y,lasty,y-lasty);
	p.push([0.8,y-lasty])
	lasty = y;
    }
    return p;
}
function sigmoid_connect(flen,xstart,yc,sl,m,doc) {
    /* sigmoid static set*/
    //doc.text("a",xstart,150)
    var ax = export_schema;    
    var lasty = flen*(1/(1+Math.exp(0.5*8)));
    var p = sigmoid(flen);
    doc.setLineWidth(0.6);
    doc.setDrawColor(70,130,180);
    doc.setFillColor(176, 196, 222);

    doc.lines(p,xstart,yc)
    if(sl) {
	doc.line(xstart,yc,xstart+40,yc);
	doc.setFont("courier",'normal');
	doc.setFontSize(10);
	doc.text(ax.decisions_table[1][m],xstart+24,yc-1)
    }
    f = p.map(x=> [x[0],-1*x[1]])
    doc.lines(f,xstart,yc)

    //doc.circle(xstart,yc,3,"FD")
    /*  Non edges nodes will use this color*/
    d_fillColor = "#b0c4de";
    d_drawColor = "#4682b4";
    circles.push([xstart,yc,3,"FD",d_drawColor,d_fillColor])
}
function find_nemos(cdp) {
    var xy = [[]];
    var clabels = cdp.children
    
    var [x,y] = export_schema.decision_points.reduce( (g,h) => {
	var m = clabels.findIndex((p) => h.label == p.label);
	if( m > -1) {
	    h.options.forEach((u) => {
		if(!g[m]) g[m] = [];
		g[m].push(u.label)
	    });
	}
	return g;
    }, [])
    cdp.options.forEach((d) => {
	d.child_combinations.forEach((p) => {
	    var j = -1,i = -1,is = [], js = [];
	    p.forEach((r) => {
		r.child_option_labels.forEach((s) => {
		    if(r.child_label == clabels[0].label)
			i = x.findIndex(m => m == s)
		    else
			j = y.findIndex(m => m == s)
		    if(i > -1)
			is.push(i)			
		    if(j > -1)
			js.push(j)
		})
		is.forEach((it)  => {
		    js.forEach((jt) => {
			if(!xy[it])
			    xy[it] = [];
			xy[it][jt] = d.label;
		    })
		})
	    })
	})
    })
    console.log(xy);
}    
function make_complex_table(cdp,doc,ynow,clabels) {
    /* Give it a complex decision point CDP */
    var xy = [[]];
    
    var [x,y] = export_schema.decision_points.reduce( (g,h) => {
	var m = clabels.findIndex((p) => h.label == p);
	if( m > -1) {
	    h.options.forEach((u) => {
		if(!g[m]) g[m] = [];
		g[m].push(u.label)
	    });
	}
	return g;
    }, [])
    cdp.options.forEach((d) => {
	d.child_combinations.forEach((p) => {
	    var j = -1,i = -1,is = [], js = [];
	    p.forEach((r) => {
		r.child_option_labels.forEach((s) => {
		    if(r.child_label == clabels[0])
			i = x.findIndex(m => m == s)
		    else
			j = y.findIndex(m => m == s)
		    if(i > -1)
			is.push(i)			
		    if(j > -1)
			js.push(j)
		})
		is.forEach((it)  => {
		    js.forEach((jt) => {
			if(!xy[it])
			    xy[it] = [];
			xy[it][jt] = d.label;
		    })
		})
	    })
	})
    })
    console.log(xy);    
    doc.setFont("helvetica","bold");
    doc.setFontSize(12);
    y.splice(0,0,"X")
    
    var headers = [];
    var cellwidth = parseInt(160/y.length);
    var fullwidth = cellwidth*y.length;
    for (var i = 0; i < y.length; i += 1) {
	var tf = {
	    name: y[i],
	    prompt: y[i],
	    width: cellwidth,
	    align: "center",
	    padding: 0
	}
        headers.push(tf);
    }


    var result = [y.reduce((a,f) =>{ a[f] = f; return a; },{})]
    var data = {}
    for (var i = 0; i < x.length; i += 1) {
	data[y[0]] = x[i];
	for(var j = 0; j < xy[i].length; j++) {
	    data[y[j+1]] = xy[i][j];
	}
        result.push(Object.assign({}, data));
    }
    doc.setFont("helvetica","bold");
    doc.setFontSize(14);
    doc.setFillColor("#c7c7c7")
    /* Horizontal title */
    doc.rect(50,ynow,120,15,"FD")
    
    doc.text(clabels[1],70,ynow+10)
    doc.setFillColor("#c7c7c7")
    /* verticular title */
    doc.rect(20,ynow,30,17.5*y.length,"FD")
    ynow = ynow +15;
    if(clabels[0].length > 8) {
	clabels[0] = clabels[0].replace(" ","\n");
    }
    doc.text(clabels[0],21,ynow+15,0)
    doc.setFont("courier","italic");
    doc.setFontSize(10);
    doc.table(50, ynow, result, headers, { autoSize: false,
					   printHeaders:false });
    //doc.text("FF",15,ynow+55)
    return ynow+55;
}

function appendtree(doc,dfilename) {
    /* Add the full tree in colorful fashion to the current data*/
    doc.addPage("a4");
    window.circles = [];
    var ax = export_schema;
    //ax.decision_points[ax.decision_points.length-1].options.forEach(d => { if("color" in d) colors[d.label] = d.color})
    doc.setFontSize(16);
    doc.setFont("helvetica",'bold');
    doc.setTextColor(0);
    var coord = $('.cover_heading_append').html().replace(/^\s+(.+)\s+/g,'$1')
    doc.text("Full SSVC Tree "+coord,10,10);
    /* top left corner */
    var tlc = 180;
    var gap = 8;
    /* Mark the children that should be ignored */
    var mdecision_points = ax.decision_points.filter(
	x => (!(x.label in ischild)))
    
    for(var index=0; index < ax.decisions_table.length; index++) {
	var yc  = 10+gap*index ;
	var fillColor = "#b0c4de";
	var drawColor = "#4682b4";
	/* Gloabl values to sigmoid_connect can also use it*/
	var m = ax.decisions_table[index][final_keyword];
	doc.setFontSize(14)
	doc.setFont("courier",'bold');
	doc.setTextColor(0);
	if(m in lcolors) {
	    doc.setTextColor(lcolors[m]);
	    fillColor = lcolors[m];
	    // silver lining?
	    drawColor = "#505050";
	}
	doc.text(m,tlc+5, yc)
	if(index%3 == 1) {
	    doc.setFont("helvetica",'bold');
	    doc.setTextColor(0)
	    doc.setFontSize(12)
	    m = mdecision_points[mdecision_points.length-2]['label']
	    doc.text(m,tlc-55, yc-5)
	    yc = 10+gap*index ;
	    sigmoid_connect(8,tlc-40,yc,1,m,doc)
	    doc.setFont("courier",'normal');
	    doc.setFontSize(10);
	    doc.text(ax.decisions_table[0][m],tlc-10,yc-7,12)
	    doc.text(ax.decisions_table[2][m],tlc-10,yc+5,-12)
	}
	if(index%6 == 3) {
	    doc.setTextColor(0)
	    /* (r,flen,xstart,yc) */
	    doc.setFont("helvetica",'bold');
	    doc.setFontSize(12)
	    m = mdecision_points[mdecision_points.length-3]['label']
	    doc.text(m,tlc-95, yc-8)
	    yc = 6+gap*index
	    sigmoid_connect(13,tlc-80,yc,0,m,doc)
	    doc.setFont("courier",'normal');
	    doc.setFontSize(10);
	    doc.text(ax.decisions_table[0][m],tlc-60,yc-8,20)
	    doc.text(ax.decisions_table[3][m],tlc-60,yc+10,-20)
	}

	if(index%12 == 6) {
	    doc.setTextColor(0)
	    doc.setFont("helvetica",'bold');
	    /* (r,flen,xstart,yc) */
	    doc.setFontSize(12)
	    m = mdecision_points[mdecision_points.length-4]['label']
	    doc.text(m,tlc-130, yc-8)
	    yc = 6+gap*index
	    sigmoid_connect(26,tlc-120,yc,0,m,doc)
	    doc.setFont("courier",'normal');
	    doc.setFontSize(10);
	    doc.text(ax.decisions_table[0][m],tlc-103,yc-9,45)
	    doc.text(ax.decisions_table[6][m],tlc-103,yc+5,-45)
	}

	if(index%36 == 18) {
	    doc.setTextColor(0)
	    /* (r,flen,xstart,yc) */
	    doc.setFont("helvetica",'bold');
	    doc.setFontSize(12)
	    m = mdecision_points[mdecision_points.length-5]['label']
	    doc.text(m,tlc-170, yc-5)
	    yc = 10+gap*index ;
	    sigmoid_connect(101,20,150,1,m,doc)
	    doc.setFontSize(10);
	    doc.text(ax.decisions_table[0][m],40,yc-50,75)
	    doc.text(ax.decisions_table[12][m],40,yc+50,-75)
	}
	yc = 10+gap*index ;
	doc.setLineWidth(0.6);
	doc.setDrawColor(drawColor);
	doc.setFillColor(fillColor);
	circles.push([tlc,yc,3,"FD",drawColor,fillColor])
	//doc.circle(tlc,yc,3,"FD");
    }
    //doc.circle(circles[0][0],circles[0][1],circles[0][2],circles[0][3])
    circles.forEach((x) => {
	doc.setDrawColor(x[4]);
	doc.setFillColor(x[5]);
	doc.circle(x[0],x[1],x[2],x[3])
    });
    //console.log(circles);
    //console.log(typeof(doc.circle))
    doc.addPage("a4");
    var ynow = 10;
    var q = 0;
    doc.setFontSize(16);
    doc.setFont("helvetica",'bold');
    doc.setTextColor(0);
    doc.text("Full SSVC Tree "+coord+" definitions",10,10);
    var childlabels = ["",""]; 
    export_schema.decision_points.forEach(function(x,ix) {
	if(ynow > 230) {
	    doc.addPage("a4");
	    ynow = 20
	}
	//return 0;
	doc.setFont("helvetica",'bold');
	doc.setTextColor(0,0,0);
	ynow = ynow + 10;
	doc.setFontSize(14);
	doc.text(x.label,20,ynow);
	if(x.label in isparent) {
	    /* Add a statement on cummulative score*/
	    doc.setFont("courier","normal");
	    doc.setFontSize(12);	    
	    var p = isparent[x.label];
	    var istring = "Note: This is a cummulative score of \"";
	    p.forEach((x,ik) => {
		if('label' in x) {
		    childlabels[ik] = x.label
		    var t = current_score.forEach(
			(b) => {
			    if(x.label in b) {
				istring += x.label + "\" and \"";
			    }
			},"");
		    }
	    })
	    /* Replace the string with cummulative information */
	    istring = istring.slice(0,-6) +".";
	    var f = istring.match(/.{1,65}(\s|$)/g);
	    for (var j = 0; j<f.length; j++) {
		doc.setFont("courier",'italic')
		ynow = ynow +5
		doc.text(f[j],20,ynow);
	    }	    
	    ynow = ynow + 5;
	    ynow = make_complex_table(x,doc,ynow,childlabels);
	}
	x.options.forEach(function(y) {
	    if(ynow > 230) {
		doc.addPage("a4");
		ynow = 20
	    }	    
	    ynow = ynow + 5
	    doc.setTextColor(0x17,0xa2,0xb8);
	    doc.setFont("courier","bolditalic");
	    doc.setFontSize(12);
	    if(y.label in lcolors) 
		doc.setTextColor(lcolors[y.label]);
	    var clabel = y.label[0].toUpperCase()+y.label.substr(1);
	    doc.text(clabel,20,ynow);
	    doc.setTextColor(0,0,0);
	    var tinfo = y.description;
	    var f = tinfo.match(/.{1,45}(\s|$)/g);
	    doc.setFont("courier",'normal');
	    q = doc.getStringUnitWidth(clabel)
	    doc.text("=> "+f[0],20+q*5,ynow);
	    if(tinfo.length<= f[0].length) {
		ynow = ynow + 6
		return
	    }
	    //console.log(t[i].substr(f[0].length));
	    f = tinfo.substr(f[0].length).match(/.{1,65}(\s|$)/g);
	    for (var j = 0; j<f.length; j++) {
		doc.setFont("courier",'normal')
		ynow = ynow +5
		doc.text(f[j],20,ynow);
	    }
	    ynow = ynow+6
	});
	ynow = ynow + 0

	if(ix == export_schema.decision_points.length-1)
	    doc.save(dfilename);
    });
    
}
function triggerDownload (dataURI,fname,el) {
    var evt = new MouseEvent('click', {
	view: window,
	bubbles: false,
	cancelable: true
    })
    var a = document.createElement('a');
    a.setAttribute('download', fname)
    a.setAttribute('href', dataURI)
    a.setAttribute('target', '_blank')
    a.dispatchEvent(evt);
    $(el).attr('href',dataURI)
    $(el).attr('download',fname)
    $(el).attr('onclick',null)
}
function make_png(nodownload,nextfun) {
    var linecolor = 'white'
    var fillcolor = 'black'
    $('.link').css({'fill-opacity': 0.01,stroke: fillcolor,'stroke-width':'6px'})
    $('circle').css({fill: '#B0C4DE',stroke: fillcolor,'stroke-width':'6px'})
    $('svg.mgraph').height('200px')
    $('#graph text').css({fill: "#6d426d","font-weight":"bold"});
    $('#graph textPath').css({fill: "black",
			      stroke:"#007bff",
			      "font-weight":"normal"});
    var svg = document.querySelector('svg.mgraph')
    var canvas = document.getElementById('canvas')
    $('svg.mgraph').css({background: '#f5f5f5'})
    var width = $('svg.mgraph').width()*2
    var height = $('svg.mgraph').height()*2
    canvas.width = width
    canvas.height = height
    var ctx = canvas.getContext('2d');
    var data = (new XMLSerializer()).serializeToString(svg);
    var DOMURL = window.URL || window.webkitURL || window;
    var img = new Image()
    var svgBlob = new Blob([data], {type: 'image/svg+xml;charset=utf-8'})
    var url = DOMURL.createObjectURL(svgBlob)
    var dfname = "exporter.png"
    img.onload = function () {
	ctx.clearRect ( 0, 0, width, height );
	ctx.drawImage(img, 0, 0,width,height);
	DOMURL.revokeObjectURL(url);
	var imgURI = canvas
	    .toDataURL('image/png')
	    .replace('image/png', 'image/octet-stream')
	if(nodownload)
	    $('#pngblob').val(imgURI.split(";")[1].replace("base64,",""))
	else
	    triggerDownload(imgURI,dfname,'#dlsvg')
	if(typeof(nextfun) == "function")
	    nextfun()
    }
    img.src = url
    return url
}

function copym(containerid,ispurl) {
    var container = $(containerid)[0];
    if(!container)
	return 
    if (document.selection) {
	var range = document.body.createTextRange();
	range.moveToElementText(container);
	range.select().createTextRange();
	document.execCommand("copy");
    } else if (window.getSelection) {
	var range = document.createRange();
	range.selectNode(container);
	window.getSelection().addRange(range);
	document.execCommand("copy");
    }
    if(ispurl)
	topalert("SSVC permalink copied to clipboard","success")
    else
	topalert("SSVC vector copied to clipboard","success")
    if (window.getSelection)
	window.getSelection().removeAllRanges();
    else if (document.selection)
	document.selection.empty();
    else
	console.log("What kind of machine are you?");
    $('.permalink').addClass('d-none');    
}

function svgzoom(w) {
    var f = w.value/w.max;
    $('svg.mgraph').css({transform: "scale("+String(f)+")"});
}
