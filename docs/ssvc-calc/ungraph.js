/*
 * Copyright (c) 2025 Carnegie Mellon University.
 * NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
 * ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
 * CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
 * EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
 * NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
 * MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
 * OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
 * ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
 * PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
 * Licensed under a MIT (SEI)-style license, please see LICENSE or contact
 * permission@sei.cmu.edu for full terms.
 * [DISTRIBUTION STATEMENT A] This material has been approved for
 * public release and unlimited distribution. Please see Copyright notice
 * for non-US Government use and distribution.
 * This Software includes and/or makes use of Third-Party Software each
 * subject to its own license.
 * DM24-0278
 */

/* SSVC code for no graphics implementation of SSVC calculator */
const ungraph_libversion = "1.1.4"
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
	dt_start();
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
		      'class': 'radiogaga sl-'+fs}
	var fselect = $('<div>').attr(fsattr)
	    .append('<!-- Select -->');
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
	    $('div#'+fsattr.id).append($('<div/>').append($('<input/>').attr({
		"type":"radio",
		"name": fsattr.id,
		"data-label": x.label,
		"onclick": "ugchoose(this,false)",
		"parentname": x.label,
		"class":"form-check-input margtop prechk-"+y.label.toLowerCase(),
		"value": y.label})).append(
		    $('<label>').addClass("h3").html(y.label).on("click",function() {
			$(this).siblings().click();
		    })
		)).addClass("text-left");
	});
	if(x.decision_type == "complex") {
	    $('div#'+fsattr.id).attr('data-moptions',JSON.stringify(x));
	    $('.t-'+fs).hide();
	    if('children' in x) 
		x.children.forEach(y => {
		    $('.sl-'+safedivname(y.label)+" input.margtop").addClass('isChild')
			.attr('data-parent',x.label);
		    
		})
	}
	if(x.decision_type == "final") {
	    $('div#'+fsattr.id).hide().addClass('final-select');
	    if((plparts.length > 2) && (plparts[3] == "Simple")) 
		permalink_ungraph();
	}
    })
}
function ugchoose(w,reset) {
    var sid = parseInt(w.name.replace('isl-',''));
    var nodename = $(w).data('label');
    $(w).parent().siblings().removeClass("selected");
    $(w).parent().addClass("selected");
    var nodevalue = $(w).val();
    if(nodevalue == "Select")
	return;
    if(isNaN(sid)) return;
    current_score[sid] = {};
    current_score[sid][nodename] = nodevalue;    
    if($(w).hasClass('isChild')) {
	var parent = $(w).data('parent');
	var pselect = '[data-parent="'+parent+'"]';
	var mcdata = {};
	var cells = [];
	$(pselect).each(function(_,d) {
	    if($(d).val() == "Select")
		return;
	    if($(d).is(":checked")) {
		mcdata[$(d).data('label')]= $(d).val();
		cells.push($(d).parent().index());
	    }
	});
	$(pselect).each(function(_,x) {
	    if(cells.length < 2) 
		return;
	    var sparent = $('.sl-'+safedivname(parent))
	    var mpdata = sparent.data('moptions');
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
	    sparent.val(result);
	    /* Update the sid to be cummulative one*/
	    var tsid = parseInt(sparent.attr('id').replace('isl-',''));
	    if(!isNaN(tsid))
		sid = tsid;
	    current_score[tsid] = {};
	    current_score[tsid][parent] = result;
	    /* Determine how many columns to the left */
	    var findex = current_score.length - 1 - cells.length;
	    var ugid = "ugftr-"+String(findex);
	    /* remove earlier score if present */
	    var tdcolspan = findex;
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
	if(found) {
	    export_show();
	    return;
	}
	var d = Object.keys(x);
	var match = 0;
	for(var j=0; j< d.length; j++) {
	    if(xy[d[j]] == x[d[j]])
		match++
	}
	if(match == d.length - 1) {
	    found = true;
	    export_show();
	    var fselect = $('div.final-select');
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
function permalink_ungraph() {
    var fm=plparts[0].split("/");
    /* Last two values in this vector is timestamp and an empty string for the last
     delimiter */
    for(var i=1;i<fm.length-2;i++) {
	var dtup = fm[i].split(":");
	var fstep = export_schema.decision_points.filter(x => x.key == dtup[0]);
	if(fstep.length != 1) {
	    console.log("This decision point does not exist");
	    console.log(dtup);
	    continue;
	}
	var sfname = safedivname(fstep[0].label);
	var fopt = fstep[0].options.filter(x => x.key == dtup[1]);
	if(fopt.length != 1) {
	    console.log("This result value does not exist");
	    console.log(dtup);
	    continue;
	}
	if('children' in fstep[0]) {
	    var tdcolspan = i - 1;
	    $('#ungraph table').append($('<tr/>').addClass('trcomplex'));
	    $('.trcomplex').append($('<td>').attr('colspan',tdcolspan)
				   .html("&nbsp;"));
	    fstep[0].children.forEach(function(u) {
		/* Hide the children that we don't know the values for */
		var usfname = safedivname(u.label);
		$('.t-'+usfname).css({visibility:'visible'});
		$('#ungraph select.sl-'+usfname).hide();
		$('td.t-'+usfname).append("<p><u>Pre-select</u></p>");
	    });
	    var mbtn = $('<button>').addClass("btn btn-secondary")
		.attr('onmouseover','shwhelp(this)')
		.attr('onmouseout','hidediv(this)')
		.attr('data-tdiv',safedivname(fstep[0].label))
		.html(fstep[0].label);	    
	    var h5_id = "h5-cum-"+String(tdcolspan);
	    var msl = $('<h5>').attr("id",h5_id).html(fopt[0].label);
	    $('.trcomplex').append($('<td>').attr('colspan',2)
				   .addClass('tdcomplex tdc-'+sfname)
				   .append("<p><u>Cummulative Value</u></p>")
				   .append(mbtn).append(msl));	    
	}
	if($('#ungraph select.sl-'+sfname).val(fopt[0].label).trigger('change').length != 1) {
	    console.log("Could not make this decision "+sfname );
	}
    }
}
