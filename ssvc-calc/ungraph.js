/* SSVC code for no graphics implementation of SSVC calculator */
const ungraph_libversion = "1.0.9"
function checkclose() {
    $('#mpopup').hide();
}
function hidediv(d) {
    $('#mpopup').hide()
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
	$('#mwb').on('hidden.bs.modal', function (e) {
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
function swapg(w) {
    if($(w).val() == "Graphic") {
	$('.graphy').show();
	$('#ungraph').addClass('d-none');
    } else {
	ungraph();
    }
}
function ungraph() {
    $('.graphy').hide();
    $('#ungraph').removeClass('d-none');
    $('#ughtr').html('');
    $('#ugbtr').html('');
    $('.trcomplex').remove();
    current_score = [];
    export_schema.decision_points.forEach((x,i) => {
	var fs = safedivname(x.label);
	var fsattr = {'id':'isl-'+String(i),
		      'data-label': x.label,
		      'onchange': 'ugchoose(this,false)',
		      'class': 'form-control sl-'+fs}
	var fselect = $('<select>').attr(fsattr)
	    .append('<option>Select</option>');
	var mbtn = $('<button>').addClass("btn btn-secondary")
	    .attr('onmouseover','shwhelp(this)')
	    .attr('onmouseout','hidediv(this)')
	    .attr('data-tdiv',fs)
	    .html(x.label);
	$('#ughtr').append($('<th>').html(mbtn).addClass('t-'+fs));
	$('#ugbtr').append($('<td>').append(fselect).addClass('t-'+fs));
	if(i>0) {
	    $('.t-'+fs).css('visibility','hidden');
	}
	x.options.forEach((y,j) => {
	    $('select#'+fsattr.id).append($('<option/>').attr({
		value:y.label}).text(y.label))
	})
	if(x.decision_type == "complex") {
	    console.log(x);
	    $('select#'+fsattr.id).attr('data-moptions',JSON.stringify(x));
	    $('.t-'+fs).hide();
	    if('children' in x) 
		x.children.forEach(y => {
		    $('.sl-'+safedivname(y.label)).addClass('isChild')
			.attr('data-parent',x.label);
		    
		})
	}
	if(x.decision_type == "final") {
	    $('select#'+fsattr.id).hide().addClass('final-select');

	}
    })
}
function ugchoose(w,reset) {
    var sid = parseInt(w.id.replace('isl-',''));
    var nodename = $(w).data('label');
    var nodevalue = $(w).val();
    if(nodevalue == "Select")
	return;
    if(isNaN(sid)) return;
    current_score[sid] = {};
    current_score[sid][nodename] = nodevalue;    
    if($(w).hasClass('isChild')) {
	console.log(w);
	var parent = $(w).data('parent');
	var pselect = 'select[data-parent="'+parent+'"]';
	var mcdata = {};
	var cells = [];
	$(pselect).each(function(_,d) {
	    if($(d).val() == "Select")
		return;
	    mcdata[$(d).data('label')]= $(d).val()
	    cells.push($(d).parent().index());
	});
	$(pselect).each(function(_,x) {
	    if(cells.length < 2) 
		return;
	    var sparent = $('.sl-'+safedivname(parent))
	    var mpdata = sparent.data('moptions');
	    console.log('Ready');
	    console.log(mpdata);
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
	    console.log(result);
	    sparent.val(result);
	    /* Update the sid to be cummulative one*/
	    var tsid = parseInt(sparent.attr('id').replace('isl-',''));
	    if(!isNaN(tsid))
		sid = tsid;
	    current_score[tsid] = {};
	    current_score[tsid][parent] = result;
	    var findex = cells.sort().shift();
	    var ugid = "ugftr-"+String(findex);
	    /* remove earlier score if present */
	    var tdcolspan = findex
	    if($('.trcomplex').length < 1) {
		$('#ungraph table').append($('<tr/>').addClass('trcomplex'));
		$('.trcomplex').append($('<td>').attr('colspan',tdcolspan)
				       .html("&nbsp;"))

	    }
	    var mbtn = $('<button>').addClass("btn btn-secondary")
		.attr('onmouseover','shwhelp(this)')
		.attr('onmouseout','hidediv(this)')
		.attr('data-tdiv',safedivname(parent))
		.html(parent);
	    var h5_id = "h5-cum-"+String(findex);
	    var fsy = safedivname(nodename);
	    if($('#'+h5_id).length > 0)
		$('#'+h5_id).html(result);
	    else { 
		var msl = $('<h5>').attr("id",h5_id).html(result);
		$('.trcomplex').append($('<td>').attr('colspan',2)
				       .addClass('tdcomplex tdc-'+fsy)
				       .append("<p><u>Cummulative Value</u></p>")
				       .append(mbtn).append(msl));
	    }
	    /* Double next needed for this step with complex decision made*/
	    $('.t-'+fsy).next().next().css('visibility','visible');
	});
    }
    var nextsid = sid + 1
    if(reset == true) {
	for(var i=nextsid; i<export_schema.decision_points.length; i++) {
	    var fs = safedivname(export_schema.decision_points[i].label);
	    $('.t-'+fs).css('visibility','hidden');
	    $('#isl-'+String(i)).val('Select');
	    $('#h5-cum-'+String(i)).remove();
	    $('.tdc-'+fs).remove();
	}
    } else {
	for(var i=nextsid+1; i<export_schema.decision_points.length; i++) {
	    var fs = safedivname(export_schema.decision_points[i].label);
	    if($('.t-'+fs).css('visibility') == 'visible') {
		if(confirm("Are you sure you want to revert the decision at: "+
			   nodename+"?")) {
		    ugchoose(w,true);
		} else {
		    return;
		}
	    }
	}
    }
    if(nextsid == export_schema.decision_points.length - 1)
	make_decision()
    var fsx = safedivname(nodename);
    $('.t-'+fsx).next().css('visibility','visible');
}
function make_decision() {
    var xy = {};
    var found = false;
    current_score.forEach((d) => {
	m = Object.keys(d).shift();
	if($('.sl-'+safedivname(m)).hasClass('isChild'))
	    return;
	else 
	    xy[m] = d[m];
    })

    var xfinal = export_schema.decisions_table.find( function(x) {
	if(found)
	    return;
	var d = Object.keys(x);
	var match = 0;
	for(var j=0; j< d.length; j++) {
	    if(xy[d[j]] == x[d[j]])
		match++
	}
	if(match == d.length - 1) {
	    found = true;
	    var fselect = $('select.final-select');
	    var flabel =  fselect.data('label');
	    var fvalue = x[flabel]
	    var tprops = { border: '1px solid #ffa700',padding: '3px',borderRadius:'2px'};
	    if(fvalue in lcolors)
		tprops['border'] = '1px solid '+lcolors[fvalue];
	    var fs = safedivname(flabel);
	    $('.t-'+fs).css('visibility','visible');
	    if($('h4.hfinal').length == 1)
		$("h4.hfinal").css(tprops).html(fvalue);
	    else
		fselect.after($("<h4>").css(tprops).addClass('hfinal').html(fvalue));
	    /* return true is like break the loop */
	    return true;
	}
	return false;
    })
}
