const graphModule = (function() {
    const showFullTree = true;
    const acolors = [  "#28a745", "#72b741", "#b0c13f", "#e6be3d", "#ffc107",
		       "#fba145", "#f37d4f", "#e65b53", "#d93f4e", "#dc3545"];
    const lcolors = {};
    let raw;
    let treeData;
    let selector = '#graph';
    
    function setSelector(newSelector) {
            selector = newSelector;
    }
    
    function create_raw(dt) {
	const kmap = {};
	Object.entries(dt.decision_points).forEach(([k, v]) => {
	    kmap[k] = v.name;
	});
	function find_value(k, dp) {
	    let dpm = dp.values.find(dpv => dpv.key == k);
	    if(dpm)
		return dpm.name;
	}
	let thash = {};
	let dps = Object.keys(dt.decision_points);
	let yraw = dps.map(x => []);
	let zraw = [];
	const final_k = dt.outcome;
	const dpo = dt.decision_points[final_k];
	const ocolors = arrayReduce(acolors,dpo.values.length);
	dpo.values.forEach(function(dpv,i) {
	    lcolors[dpv.name] = ocolors[i];
	});
	dt.decision_points[final_k].values.forEacj
	const final_keyword = dt.decision_points[final_k].name;
	const mapping = dt.mapping;
	let id = 1;
	for(let i=0; i <dt.mapping.length; i++) {
	    const lhs = find_value(dt.mapping[i][final_k], dt.decision_points[final_k]);
	    let tname = lhs +":"+
		dps.map(t => find_value(dt.mapping[i][t],dt.decision_points[t]))
		.slice(0,-1).join(":");
	    for( let j=0; j< dps.length-1; j++) {
		const tparent = dt.decision_points[dps[dps.length-2-j]].name + ":" +
		      dps.slice(0,dps.length-2-j).map(q =>
			  find_value(dt.mapping[i][q],dt.decision_points[q])).join(":");
		if(!(tname in thash))
		    var yt = {name:tname.replace(/\:+$/,''),
			      id:id++,
			      parent:tparent.replace(/\:+$/,''),
			      props:"{}",children:[]}
		else
		    continue
		thash[yt.name] = 1;
		tname = tparent;
		yraw[j].push(yt);
	    }
	}
	for(var j=yraw.length; j> -1; j--)  {
	    if(yraw.length > 0)
		zraw = zraw.concat(yraw[j])
	}
	zraw[0] = {name:dt.decision_points[dps[0]].name,id:id+254,children:[],parent:null,props:"{}"}
	return zraw;
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

    function draw_graph() {
	var margin = {top: 20, right: 120, bottom: 20, left: 120},
	    width = 1060 - margin.right - margin.left,
	    height = 800 - margin.top - margin.bottom
	if(showFullTree) {
	    var add_offset = 0
	    if(raw.length > 60)
		add_offset = (raw.length - 60)*10
	    height = Math.max(1300, raw.length * 20) - margin.top - margin.bottom + add_offset
	}
	duration = 750
	tree = d3.layout.tree()
	    .size([height, width]);

	diagonal = d3.svg.diagonal()
	    .projection(function(d) { return [d.y, d.x]; });

	var default_translate =  "translate(" + margin.left + "," + margin.top + ")"
	var svg_width = width + margin.right + margin.left
	var svg_height = height + margin.top + margin.bottom
	if(window.innerWidth <= 1000) {
	    default_translate =  "translate(10,0) scale(0.75)"
	    if(window.innerWidth <= 750)
		default_translate =  "translate(30,0) scale(0.42)"
	}
	let zdiv = $('<div>').css({position: "absolute"});
	let zinp = $('<input>').attr({type: 'range',
				      min: '0',
				      max: '100',
				      value: '100',
				      accentColor: 'lightskyblue',
				      orient: 'vertical',
				      alt: 'Zoom Graph',
				      title: 'Zoom Graph'});
	zinp[0].onclick = function() {
	    const zf = this.value/this.max;
	    const fh = parseInt($('svg.mgraph').attr("height"));
	    const fw = parseInt($('svg.mgraph').attr("width"));
	    const vbox = "0 0 "+String(parseInt(fw/zf)) + " " + String(parseInt(fh/zf))
	    $('svg.mgraph').attr('viewBox',vbox);
	}
	$(selector).html('').append(zdiv.append(zinp));
	svg = d3.select(selector).append("svg")
	    .attr("xmlns","http://www.w3.org/2000/svg")
	    .attr("preserveAspectRatio","none")
	    .attr("class","mgraph")
	    .attr("width", svg_width)
	    .attr("height", svg_height)
	    .attr("viewBox", "0 0 " + svg_width + " " + svg_height)
	    .append("g")
	    .attr("transform", default_translate)
	    .attr("id","pgroup");

	root = treeData[0];
	root.x0 = height / 2;
	root.y0 = 0;

	update(root)

	d3.select(self.frameElement).style("height", "700px");
    }

    function update(source) {
	var i = 0
	var nodes = tree.nodes(root).reverse()
	var links = tree.links(nodes)

	nodes.forEach(function(d) { d.y = d.depth * 200;})

	var node = svg.selectAll("g.node")
	    .data(nodes, function(d) { return d.id || (d.id = ++i); });

	var nodeEnter = node.enter().append("g")
	    .attr("class", "node bof")
	    .attr("transform", function(d) {
		return "translate(" + source.y0 + "," + source.x0 + ")";
	    })
	    .attr("class", function(d) {
		var finale = "";
		if(!('children' in d))
		    finale = " finale";
		if('depth' in d)
		    return "node depth-"+String(d.depth)+finale;
		return "node depth-none";})
	    .on("click", doclick)
	    .on("contextmenu",dorightclick)
	    .on("mouseover",showdiv)
	    .on("mouseout",hidediv);
	nodeEnter.append("circle")
	    .attr("r", 1e-6)
	    .attr("class",function(d, i) {
		if(!('children' in d))
		    return "junction gvisible finale ";
		return "junction gvisible"
	    })
	    .style("fill", function(d, i) {
		if(d._children) return "lightsteelblue"
		if(!('children' in d)) {
		    /* Last node no children */
		    var dname = d.name.split(":").shift();
		    if(dname in lcolors)
			return undefined;
		}
		return undefined;
	    }  );

	var font = "20px"
	if(showFullTree)
	    font = "18px"
	nodeEnter.append("text")
	    .attr("x",function(d) { return check_children(d,"-55","+20") })
	    .attr("y",function(d) { return check_children(d,"-37","0") })
	    .attr("dy", ".35em")
	    .attr("class",function(d) {
		var fclass = d.name.split(":").shift().toLowerCase();
		if(!('children' in d))
		    return "gvisible prechk-"+fclass+" finale";
		return "gvisible prechk-"+fclass;})
	    .text(function(d) { return d.name.split(":")[0]; })
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

	var nodeExit = node.exit().transition()
	    .duration(duration)
	    .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
	    .remove();

	nodeExit.select("circle")
	    .attr("r", 1e-6);

	nodeExit.select("text")
	    .style("fill-opacity", 1e-6);

	var link = svg.selectAll("path.link")
	    .data(links, function(d) { if(d.target) return d.target.id; })
	link.enter().insert("path","g")
	    .style("fill","none").style("stroke", "#ccc").attr("class","link")
	    .attr("id", function(d) { return 'l'+Math.random().toString(36).substr(3); })
	    .attr("kdata", function(d) { return d.source.name.split(":").shift(); })
	    .attr("ldata", function(d) { return d.target.name.split(":").pop(); })
	    .attr("ldeep", function (d) { return d.target.name.split(":").length })
	    .attr("csid",function(d) { return d.target.id;})
	    .attr("d", function(d) {
		var o = {x: source.x0, y: source.y0};
		return diagonal({source: o, target: o});
	    })

	link.transition()
	    .duration(duration)
	    .attr("d", diagonal);

	link.exit().transition()
	    .duration(duration)
	    .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	    })
	    .remove();

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
	var xMin = d3.min(nodes, function(d) { return d.x; });
	var xMax = d3.max(nodes, function(d) { return d.x; });

	var yOffset = 90;
	var xOffset = -xMin + yOffset;
	var newHeight = xMax - xMin + 2 * yOffset;
	if (newHeight > parseInt($('svg.mgraph').attr("height"))) {
	    $('svg.mgraph').attr("height", newHeight);
	}
	svg.attr("transform", "translate(" + 100 + "," + xOffset + ")");
    }
    function check_children(d,a,b) {
	if((d.children) && (d.children.length)) return a
	if((d._children) && (d._children.length)) return a
	return b
    }

    function arrayReduce(arr,n) {
	if(n > arr.length)
	    return arr.concat(Array(n-arr.length).fill(arr.at(-1)))
	return arr.filter(function(_,i) {
	    if (i === 0 || i === arr.length - 1) return true;
	    const step = (arr.length-1)/(n-1);
	    for (let j = 1; j < n - 1; j++)
		if (Math.round(j * step) === i)
		    return true;
	    return false;
	});
    }
    
    function dt_graph(dt) {
	raw = create_raw(dt);
	treeData = grapharray_open(raw);
	draw_graph();
    }

    function update_links() {
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
		.append("path").attr("d",xd).attr("id","f"+id)
		.style("fill","none").style("stroke","#ccc")
		.attr("class","xlink");
	    var doffset = parseInt(70 - (4-depth)*5.5)
	    var yoffset = -10
	    if(showFullTree)
		yoffset = -6
	    d3.select("g#x"+id).append("text").attr("dx",-6).attr("dy",yoffset).attr("class","gtext")
		.append("textPath").attr("href","#f"+id).attr("class",xclass)
		.attr("text-anchor","middle")
		.attr("id","t"+id)
		.attr("csid",csid)
		.attr("parentname",pname)
		.text(text).attr("startOffset",doffset+"%")
		.on("click",pathclick)
		.on("mouseover",showdiv)
		.on("mouseout",hidediv);
	});
    }
    function graph_dynamic(input) {
	const dpContainer = input.parentElement.parentElement.parentElement;
	const finddpIndex = $(input).data("dpdepth");
	const nodes = d3.selectAll("g.node.depth-"+String(finddpIndex));
	function traverse_remove(xnode) {
	    if(!xnode.__data__) {
		console.log("Error no nodes to descend!");
	    }
	    if(!xnode.__data__._schildren) {
		console.log("Error no node _schildren data to restore from!");
	    }
	    let removeValues = [];
	    xnode.__data__.children = Array.from(xnode.__data__._schildren);
	    dpContainer.querySelectorAll("input").forEach(function(cinput) {
		if(!cinput.checked)
		    removeValues.push($(cinput).data("dpvdepth"));
	    });
	    removeValues.reverse().forEach(function(rindex) {
		removevalueIndex = parseInt(rindex);
		xnode.__data__.children.splice(removevalueIndex,1);
	    });
	    update(xnode.__data__);
	}
	if(nodes.length) {
	    nodes[0].forEach(function(xnode) {
		if(xnode.__data__) {
		    if(xnode.__data__._schildren) {
			traverse_remove(xnode);
		    } else if(xnode.__data__.children) {
			let removevalueIndex = $(input).data("dpvdepth");
			xnode.__data__._schildren = Array.from(xnode.__data__.children);
			xnode.__data__.children.splice(removevalueIndex,1);
			update(xnode.__data__);
		    }
		}
	    });
	}
    }
    /* Helper function for advanced UI affects */
    function pathclick() {};
    function showdiv() {};
    function hidediv() {};
    function dorightclick() {};
    function doclick() {};
    function togglehelp() {};


    return {
	pathclick:pathclick,
	showdiv:showdiv,
	hidediv:hidediv,
	dorightclick:dorightclick,
	doclick:doclick,
	togglehelp:togglehelp,
	graph_dynamic: graph_dynamic,
	dt_graph: dt_graph,
	setSelector: setSelector,
	__version__: "1.0.10"
    };
})();

const SSVC = (function() {
    let outcomes =  [];
    let results = {};
    let decision_points =  [];
    let decision_trees =  [];
    let form =  null;
    let dpMap = {};
    let default_namespace = "x_com.example#psirt";
    let namespaces = [];
    let __version__ = "1.0.12";
    
function niceString(str) {
    if (str.length)
	return str.charAt(0).toUpperCase() + str.slice(1);
    return "";
}
function add_dash_n(str, strSet) {
    if(!(str in strSet))
	return str;
    const regex = /(-\d+)$/;
    const match = str.match(regex);
    let newNumber = -1;
    let nstr = str + newNumber.toString();
    if (match) {
	const numberPart = parseInt(match[1], 10); 
	newNumber = numberPart - 1;
	nstr = str.replace(regex, newNumber.toString());
    } 
    while(nstr in strSet) {
	newNumber = newNumber - 1;
	nstr = str.replace(regex, newNumber.toString());
    }
    return nstr;
}
function name_version(obj) {
    if(obj.name && obj.version)
	return obj.name + " (" + obj.version + ")";
    else if (obj.name)
	return obj.name + " (0.0.1)";
    else
	return "";
}
function dtreeSort(a, b) {
    const nameA = a.data.namespace.toUpperCase() + a.data.name.toUpperCase()
	  + a.data.version.toUpperCase();
    const nameB = b.data.namespace.toUpperCase() + b.data.name.toUpperCase()
	  + b.data.version.toUpperCase();
    if (nameA < nameB) 
	return -1;
    if (nameA > nameB)
	return 1;
    return 0;
}
function simpleCopy(inobj) {
    return JSON.parse(JSON.stringify(inobj));
}
window.addEventListener("beforeunload", function(e) {
    if(sessionStorage.getItem("ssvc-pending")) {
	var confirmationMessage = 'Are you sure to leave the page?';
	const event = (e || window.event);
	event.preventDefault();
	event.returnValue = confirmationMessage;
	return confirmationMessage;
    }
    return null;
});
function applyStyle(div, props) {
    Object.entries(props).forEach(function(k,_) {
	div.style[k[0]] = k[1];
    });
}
function topalert(msg, level, timeOut) {
    const colors = {
        "danger": "#dc3545",
        "info": "#0d6efd",
        "warn": "#ffc107",
        "success": "#198754"
    };

    let div = document.querySelector("[data-topalert]");
    if (!div) {
        div = document.createElement("div");
        div.setAttribute("data-topalert", "1");
        const props = {
            width: "100%",
            top: "0px",
            left: "0px",
            "text-align": "center",
            color: "white",
            border: "2px solid transparent",
            "border-radius": "4px",
            padding: "12px",
            opacity: 0,
            "font-size": "1.2em",
            "transition": "opacity 0.5s ease",
            "z-index": "9999",
            "background-color": "transparent",
            position: "relative"   
        };
        applyStyle(div, props);
        document.body.prepend(div);
    }

    if (!msg) {
        div.style.opacity = 0;
        div.style.backgroundColor = "transparent";
        div.innerHTML = "";
        return;
    }

    div.innerHTML = ""; 
    div.innerText = msg + " ";

    const span = document.createElement("span");
    span.innerHTML = "&#x2715;";
    applyStyle(span, {
        cursor: "pointer",
        color: "white",
        padding: "2px 6px",
        border: "1px solid white",
        "border-radius": "2px",
        margin: "3px"
    });
    div.appendChild(span);

    div.onclick = () => div.remove();

    div.style.backgroundColor = colors[level] || colors["info"];
    div.style.display = "block";
    div.style.opacity = 0.95;

    if (timeOut) {
        if (div._timer) clearTimeout(div._timer);
        div._timer = setTimeout(() => {
            div.style.opacity = 0;
            setTimeout(() => div.remove(), 600); 
        }, timeOut * 1000); 
    }
}


function compareObj(o1,o2) {
    const keys = Object.keys(o1);
    if(keys.length != Object.keys(o2).length)
	return false;
    for(let i=0; i < keys.length; i++) {
	const key = keys[i];
	if(o1[key] != o2[key]) {
	    return false;
	}
    }
    return true;
}
function h5button(text, current, type) {
    const h5 = document.createElement("h5");
    h5.innerText = text;
    h5.style.display = "inline-block";
    if(current)
	h5.style.backgroundColor = "#007bff";
    else
	h5.style.backgroundColor = "#555555";	      
    h5.style.padding = "2px";
    h5.style.color = "white";
    h5.style.borderRadius = "4px";
    h5.setAttribute("data-tabs", type);
    h5.addEventListener("click", function() {
	const btn = this;
	const current = btn.getAttribute("data-tabs");
	btn.parentElement.querySelectorAll("[data-tabs]").forEach(function(el) {
	    el.style.backgroundColor = "#555555";
	});
	btn.style.backgroundColor = "#007bff";
	btn.parentElement.querySelectorAll("[data-tab]").forEach(function(el) {
	    if(el.getAttribute("data-tab") == current)
		el.style.display = "block";
	    else
		el.style.display = "none";
	});
    });
    return h5;
}
function rand_namespace(dtype) {
    if(!dtype)
	dtype = "generic"
    return "x_example." + crypto.randomUUID() + "#" + dtype.toLowerCase();
}
function lock_unlock(lock) {
    const select = form.parentElement.querySelector("[id='sampletrees']");
    const btnAll = form.parentElement.querySelector("[data-toggleall]");
    if(lock) {
	const nextel = select.nextElementSibling;
	/* Add custom data entry points */
	select.style.display = "none";
	select.parentElement.children[0].innerText = "Custom Decision Model";
	if(nextel.tagName.toUpperCase() == "DIV") {
	    const inp = nextel.querySelector("input[name='namespace'");
	} else {
	    const div = document.createElement("div");
	    const clbtn = form.parentElement.querySelector("[data-clear]");
	    let dt;
	    if(clbtn.hasAttribute("data-json")) {
		dt = JSON.parse(clbtn.getAttribute("data-json"));
	    } else {
		dt = {namespace: default_namespace,
		      name: "Custom Decision Tree",
		      definition: "Uploaded Custom Decistion Tree from CSV",
		      version: "1.0.1"};
	    }
	    div.style.display = "inline-block";
	    applyStyle(div, {border: "1px dotted darkblue",
			     display: "inline-block",
			     borderRadius: "2px",
			     padding: "4px"
			    });
	    ["name","namespace","definition","version"].forEach(function(nprop) {
		const label = document.createElement("label");
		const input = document.createElement("input");
		input.name = nprop;
		const nproper = niceString(nprop);
		input.placeholder = "Decision Tree " + nproper;
		if(nprop != "namespace")
		    input.value = dt[nprop];
		else 
		    input.value = rand_namespace("decisiontables");
		applyStyle(input, {background: "transparent",
				   padding: "0px 2px",
				   display: "inline",
				   fontWeight: "bolder",
				   border: "1px solid #198754"});
		applyStyle(label, {display: "block",
				   textAlign: "right",
				   fontWeight: "bolder"});
		label.innerText = nproper + ": ";
		label.append(input);
		div.append(label);
		
	    });
	    select.after(div);
	}
	select.setAttribute("disabled", true);
	btnAll.setAttribute("disabled", true);
	btnAll.style.opacity = 0.5;
	sessionStorage.setItem("ssvc-pending",1);
    }else {
	select.parentElement.children[0].innerText = "Sample Decision Models::";
	
	if(select.nextElementSibling.nodeName.toUpperCase() == "DIV") {
	    select.nextElementSibling.remove();
	}
	select.style.display = "inline-block";
	select.removeAttribute("disabled");
	btnAll.removeAttribute("disabled");
	btnAll.style.opacity = 1.0;
	sessionStorage.removeItem("ssvc-pending");	
    }
    
}
function clear() {
    const sampletrees = form.parentElement.querySelector("[id='sampletrees']");
    const nextel = sampletrees.nextElementSibling;
    if(nextel.tagName.toUpperCase() == "DIV")
	nextel.remove();
    sessionStorage.removeItem("ssvc-pending");
    sampletrees.style.display = "inline-block";
    sampletrees.disabled = false;
    sampletrees.dispatchEvent(new Event('change'));
    const cbtn = form.parentElement.querySelector("[data-customize='1']");
    cbtn.innerHTML = "Customize";
    const btnAll = form.parentElement.querySelector("[data-toggleall]");
    btnAll.disabled = false;
    btnAll.style.opacity = 1.0;
}
function toNumberTable(table, headers) {
    const encoders = {};
    const numberTable =  table.map(function(row) {
	return headers.reduce(function(r,head) {
	    const col = row[head];
	    if(head in encoders) {
		if (!(col in encoders[head])) {
		    const max = Math.max.apply(this,Object.values(encoders[head]));
		    encoders[head][col] = max + 1;
		}
	    } else {
		encoders[head] = {};
		encoders[head][col] = 0;
	    }
	    r.push(encoders[head][row[head]]);
	    return r;
	}, []);
    });
    return numberTable;
}
function csvline(cols) {
    cols = cols.map(x => x.replace('"','\\"'))
    return '"' + cols.join('","') + '"\n';
}
function get_decision_point(name, version, namespace) {
    /* version 1.0.0 name mapping in CSV files */
    if(name in dpMap && !version) {
	version = dpMap[name]["version"]
	namespace = dpMap[name]["namespace"];
	/* Check if name is remapped in CSVs*/	
	if("name" in dpMap[name]) 
	    name = dpMap[name]["name"];
    }
    if(!version)
	version = "1.0.0";
    if(!namespace)
	namespace = "ssvc";
    for(let i = 0; i < decision_points.length; i++) {
	if(decision_points[i].data.name == name &&
	   decision_points[i].data.namespace == namespace &&
	   decision_points[i].data.version == version) {
	    return decision_points[i].data;
	}
    }
    return {};
}
function update_stats() {
    results = {};
    form.querySelectorAll("[data-outcome]").forEach(function(el) {
	let outcome;
	if(el.querySelector("input"))
	    outcome = el.querySelector("input").value	
	else
	    outcome = el.innerText;
	if(outcome in results )  {
	    if(el.parentElement.style.display != "none")
		results[outcome] += 1;

	} else {
	    if(el.parentElement.style.display != "none")
		results[outcome] = 1;
	    else
		results[outcome] = 0;
	}
    });
 
    let outcomeMax = Math.max.apply(null, Object.values(results));
    Object.keys(results).forEach( function(outcome) {
	outcome = outcome.replaceAll('"','\\"');	    
	let rlabel = form.querySelector('[data-result="'+outcome+'"] > label > span');
	rlabel.innerText = " (" + String(results[outcome]) + ")";
	let dbar = document.createElement("span");
	dbar.innerHTML = "&nbsp;";
	dbar.style.marginLeft = "6px";
	dbar.style.display = "inline-block";
	dbar.style.width = String(parseInt(70 * results[outcome]/outcomeMax)) + "px";
	dbar.style.backgroundColor = "#5480de";
	/* dbar.style.position = "fixed"; */
	rlabel.appendChild(dbar);
	
    });
    const dtstamp = (new Date()).toISOString().replace(/[^0-9a-zA-Z]/g,"-")
    const download_filename = "SSVC_Custom_" + dtstamp + "_json.txt";
    let clbutton = form.parentElement.querySelector("[data-clear]");
    let jsonTreedump = clbutton.getAttribute("data-json");
    const btn = form.parentElement.querySelector("[data-download-json]");
    btn.href = "data:text/plain;charset=utf-8,"+
	encodeURIComponent(jsonTreedump);
    btn.setAttribute("download", download_filename);
    const btncsv = form.parentElement.querySelector("[data-download-csv]");
    let CSV = form.parentElement.querySelector("[data-tab='CSV']").dataset.csv;
    if(!CSV) {
	/* Force render to ensure the elment is visible properly*/
	let tab = form.parentElement.querySelector("[data-tab='CSV']");
	let oldv = tab.style.display;
	tab.style.display = "block";
	CSV = form.parentElement.querySelector("[data-tab='CSV']").innerText;
	tab.style.display = oldv;
    }
    btncsv.href = "data:text/plain;charset=utf-8," +
	encodeURIComponent(CSV);
    const csv_filename = "SSVC_Custom_" + dtstamp + ".csv";    
    btncsv.setAttribute("download", csv_filename);
}

function createSSVC(csv, uploaded) {
    const exporter = { "ssvcV1_0_1": {
	"id": "CVE-1999-1234",
	"selections": [],
	"timestamp": (new Date()).toISOString(),
	"schemaVersion": "1-0-1"
    }};
    const ssvcTable = [];
    let jsonTree = {}
    let CSV = "";
    let outcomeTitle;
    let lines = [];
    let headers = [];
    let dset = [];
    if(typeof(csv) === "object") {
	/* This is JSON data more powerful use it */
	jsonTree = simpleCopy(csv);
	if(('schemaVersion' in jsonTree) && 
	   (jsonTree.schemaVersion === '2.0.0') &&
	   ('decision_points' in jsonTree)) {
	    if(('outcome' in jsonTree) &&
	       (jsonTree.outcome in jsonTree.decision_points)) 
		outcomeTitle = jsonTree.decision_points[jsonTree.outcome].name;
	    let hkeys = [];
	    dpMap = {};
	    let outcomeset = [];
	    Object.entries(jsonTree.decision_points).forEach(function([k,dp]) {
		/* Dynamically build the name map per Tree. Assumption is there
		   are NO two decision points with the same name */
		if(dp.name in dpMap)
		    topalert("danger", "Duplicate Names found in Decision Table can cause confusion", 0);
		dpMap[dp.name] = {name: dp.name, version: dp.version,
				       namespace: dp.namespace, data: dp};
		if(k != jsonTree.outcome) {
		    dset.push(dp.values.map(x => x.name));
		    headers.push(dp.name);
		    hkeys.push(k);
		} else {
		    /* Make sure the dset has the last entry as outcome*/
		    outcomeset = dp.values.map(x => x.name);
		}
	    });
	    dset.push(outcomeset);
	    headers.push(outcomeTitle);
	    hkeys.push(jsonTree.outcome);
	    if('mapping' in jsonTree)
		jsonTree.mapping.forEach(function(dvpair) {
		    const line = hkeys.map(function(k) {
			const vk = dvpair[k];
			const dp = jsonTree.decision_points[k];
			for(let i = 0; i < dp.values.length; i++) 
			    if(dp.values[i].key == vk) 
				return dp.values[i].name;
		    });
		    lines.push(line);
		});
	}
    } else {
	lines = csv.split('\n');
	headers = lines.shift().split(',');
	if(headers[0] == "row") {
	    /* CSV with row numbering setup so remove the first element*/
	    headers.shift();
	}
    }
    const main = document.createElement("main");
    function destroytip() {
	let div = form.querySelector("[data-temp]");
	if(div)
	    div.remove();
    }
    function tooltip(event, info) {	
	let div = form.querySelector("[data-temp]");
	if(!div) {
	    div = document.createElement("div");
	    div.setAttribute("data-temp",1);
	}
	div.innerText = info;
	const style = {
	    "display": "block",
	    "backgroundColor": "#333",
	    "opacity": "0.9",
	    "maxWidth": "300px",
	    "color": "white",
	    "borderRadius": "8px",
	    "position": "absolute",
	    "left": String(event.pageX + 10) + "px",
	    "top": String(event.pageY + 10) + "px",
	    "padding": "4px",
	    "border": "2px solid aqua"
	};
	Object.assign(div.style,style);
	form.appendChild(div);
    }
    function helptip(event) {
	let dp = {};
	/* Check for Decision Point or Outcome and return helptip */
	const isdp = ["data-dp","data-outcomename"].some(function(fdp) {
	    if(event.target.hasAttribute(fdp)) {
		/* A Decision Point help tip  */
		dp = get_decision_point(event.target.getAttribute(fdp));
		if(dp.definition) {
		    tooltip(event, dp.definition);
		    return true;
		}
	    }
	    /* This is more like continue */
	    return false;
	});
	if(isdp)
	    return false;
	/* A Decision Point value helptip */
	const dpInput = event.target.querySelector("input");
	if(dpInput) {
	    if(dpInput.parentElement.parentElement.getAttribute("data-help")) {
		dp = JSON.parse(dpInput.parentElement.parentElement.getAttribute("data-help"));
	    } else {
		dp = get_decision_point(dpInput.name);
		if(dp.definition) 
		    dpInput.parentElement.parentElement.setAttribute("data-help",JSON.stringify(dp));
	    }
	} 
	if(dp.values) {	 
	    for(let i=0; i<dp.values.length; i++) {
		if(dp.values[i].name.toLowerCase() == dpInput.value.toLowerCase()) {
		    return tooltip(event,dp.values[i].definition);
		}
	    }
	}
    }
    if(uploaded) {
	/* Remove any name conflict */
	headers.forEach(function(dpName,i) {
	    while(dpName in dpMap) {
		let idx = 1;
		dpName = dpName + "-" + idx;
		idx = idx + 1;
	    }
	    headers[i] = dpName;
	    dpMap[dpName] = {"namespace": "x_com.example#psirt",
				  "version": "1.0.0"};
	});
    }
    main.style.display = "flex";
    main.style.verticalAlign = "top";
    const allrows = document.createElement("div");
    CSV = CSV + csvline(headers);
    lines.forEach(function(line) {
	if(!line)
	    return;
	let cols;
	if(Array.isArray(line)) {
	    cols = line;
	} else {
	    cols = line.split(',');
	    if(cols[0].match(/^\d+$/)) {
		/* Remove first element of columns if they are row numbers */
		cols.shift();
	    }
	}
	CSV = CSV + csvline(cols);	
	const row = {};
	const rowDiv = document.createElement("div");
	rowDiv.style.display = "table-row";
	headers.forEach(function(dpName,i) {
	    const colDiv = document.createElement("div");
	    colDiv.innerText = cols[i];
	    colDiv.style.padding = "0px";
	    colDiv.style.border = "1px solid cyan";
	    colDiv.style.display = "table-cell";
	    if( i == headers.length - 1) 
		colDiv.setAttribute("data-outcome", cols[i]);
	    rowDiv.append(colDiv);
	    row[dpName] = cols[i];
	});
	rowDiv.style.display = "none";
	rowDiv.setAttribute("data-row",JSON.stringify(row));
	allrows.append(rowDiv);
	ssvcTable.push(row);
    });
    const rowDiv = document.createElement("div");
    rowDiv.style.display = "table-row";
    headers.forEach(function(header, i) {
	const div = document.createElement('div');
	div.style.padding = "0px";
	div.style.border = "1px solid cyan";
	div.style.display = "inline-block";
	const hdiv = document.createElement("div");
	hdiv.innerText = header;
	hdiv.style.padding = "4px";
	hdiv.style.borderBottom = "1px solid cyan";
	hdiv.style.fontWeight = "bold";
	hdiv.setAttribute("data-dp",header);
	hdiv.setAttribute("data-dpIndex",i);	
	if(i == headers.length -1 ) {
	    hdiv.setAttribute("data-outcomeName",header);
	}
	hdiv.addEventListener("mouseenter", helptip);
	hdiv.addEventListener("mouseleave", destroytip);	
	div.append(hdiv);
	const chdiv = hdiv.cloneNode(true);
	chdiv.style.border = "1px solid cyan";
	chdiv.style.display = "table-cell";
	rowDiv.appendChild(chdiv);
	if(!dset[i].length) {
	    /* We may not get the right order for CSV imports*/
	    dset[i] = ssvcTable.reduce(function(acc,row) {
		if(!acc.includes(row[header]))
		    acc.push(row[header]);
		return acc;
	    }, []);
	}
	let j = -1;
	dset[i].forEach(function(value) {
	    j++;
	    const inputDiv = document.createElement('div');
	    inputDiv.style.padding = "4px";
	    const input = document.createElement('input');
	    input.type = "checkbox";
	    input.setAttribute("data-dpdepth", i);
	    input.setAttribute("data-dpvdepth", j);
	    input.name = header;
	    const vlabel = document.createElement('label');
	    vlabel.innerText = value;
	    input.value = value; 
	    if(i ==  headers.length -1 ) {
		/* Last column for results */
		inputDiv.setAttribute("data-result",value);
		inputDiv.style.opacity = 0.6;
		outcomeTitle = header;
		inputDiv.style.fontWeight = "bolder";
		inputDiv.style.border = "1px solid cyan";
		/* inputDiv.style.position = "relative"; */
		const spanCount = document.createElement("span");
		spanCount.innerText = " ()";
		vlabel.appendChild(spanCount);
	    }
	    /* Add this except for last row
	       Last row is our results row. */
	    vlabel.addEventListener("click", function(el) {
		this.previousSibling.click();
	    });
	    inputDiv.append(input);
	    inputDiv.append(vlabel);
	    inputDiv.addEventListener("mouseenter", helptip);
	    inputDiv.addEventListener("mouseleave", destroytip);
	    div.append(inputDiv);
	});
	main.appendChild(div);
    });
    if(uploaded) {
	/*Create Custom Decision Points and add them to popup */
	const newdps = Object.keys(ssvcTable[0]).reduce(function(ac,name) {
	    if(name != outcomeTitle) {
		let version = "1.0.0";
		let namespace = "demo/custom"
		ac[name] = {"filename": "memory:" + name ,
			    "data": {"namespace": namespace,
				     "name": name,
				     "version": version,
				     "definition": name,
				     "schemaVersion": "1-0-1",
				     "values": []
				    }
			   }
	    }
	    return ac;
	}, {});
	ssvcTable.forEach(function(row) {
	    Object.keys(row).forEach(function(dpName) {
		const value = row[dpName];
		if(newdps[dpName]) {
		    if(newdps[dpName].data.values.findIndex(function(nvalue) {
			return nvalue.name == value;}) < 0) {
			newdps[dpName].data.values.push({"name": value, "definition": value, "key": value[0]});
		    }
		}

	    });
	});
	/*Append new decision points */
	decision_points.push.apply(decision_points,
					Object.values(newdps));
    }
    
    decision_table = ssvcTable;
    const numberTable = toNumberTable(decision_table,Object.keys(decision_table[0]));
    const features = [];
    const results = []
    numberTable.forEach(function(row) {
	const outcome = row.pop();
	if(results[outcome])
	    results[outcome] = results[outcome] + 1;
	else
	    results[outcome] = 1;
	results.push(outcome);
	features.push(row);
    });
    if(Object.keys(results).length > 1) {
	const labels = decision_table.map(function(x) {
	    return x[outcomeTitle];
	});
	const featureImportance = computeFI(features,labels);
	if(Object.keys(featureImportance).length == features[0].length) { 
	    const pfdiv = document.createElement("div");
	    pfdiv.style.display = "table-row";
	    for(let i=0; i < features[0].length; i++) {
		const fdiv = document.createElement("div");
		fdiv.innerText = featureImportance[i]['importance'].toFixed(4);
		fdiv.style.display = "table-cell";
		fdiv.style.border = "1px solid cyan";
		pfdiv.appendChild(fdiv);
	    }
	    const fdiv = document.createElement("div");
	    fdiv.innerText = "<= Feature Importance";
	    pfdiv.appendChild(fdiv);
	    allrows.prepend(pfdiv);
	}
    } else {
	console.log("There are no features to select importance from");
    }
    allrows.prepend(rowDiv);
    allrows.style.display = "table";
    allrows.setAttribute("data-tab","table");
    form.appendChild(main);
    form.appendChild(h5button("SSVC Table", "current", "table"));
    form.appendChild (document.createTextNode (" "));
    form.appendChild(h5button("JSON", null, "JSON"));
    form.appendChild (document.createTextNode (" "));
    form.appendChild(h5button("CSV", null, "CSV"));
    form.appendChild (document.createTextNode (" "));
    form.appendChild(h5button("Graph", null, "GRAPH"));    
    const btn = form.parentElement.querySelector("[data-clear]");
    btn.style.backgroundColor = "#dc3545";
    btn.style.color = "white";
    btn.innerText = " CLEAR ";
    btn.type = "button";
    if(typeof(csv) == "object")
	btn.setAttribute("data-json", JSON.stringify(csv,null,2));
    else
	btn.setAttribute("data-csv", csv);
    btn.addEventListener("click",clear);
    form.appendChild(allrows);
    const code = document.createElement("code");
    code.style.display = "none";
    code.style.border = "1px solid gray";
    code.style.width =  "fit-content"
    code.style.backgroundColor = "#eee";
    code.style.padding = "6px";    
    code.style.whiteSpace = "pre-wrap";
    code.style.maxWidth = "90%";
    code.setAttribute("data-tab","JSON");
    code.innerText = JSON.stringify(jsonTree, null, 4);
    form.appendChild(code);
    const tcode = code.cloneNode();
    tcode.setAttribute("data-tab","CSV");
    tcode.innerText = CSV;
    tcode.dataset.csv = CSV;
    form.appendChild(tcode);
    const tgraph = document.createElement("div");
    tgraph.id = "graph"
    tgraph.setAttribute("data-tab","GRAPH");
    tgraph.style.display = "none";
    tgraph.innerText = "Graph not available for CSV data";
    form.appendChild(tgraph);
    if(jsonTree.decision_points)
	graphModule.dt_graph(csv);
    function filterData(ev) {
	exporter.ssvcV1_0_1.selections = [];
	if(main.querySelectorAll("input:checked").length == 0) {
	    form.querySelectorAll('[data-row]').forEach(function(row) {
		row.style.display="none";
	    });
	    return update_stats();
	}
	const div = ev.target.parentElement;
	const ldivs = Array.from(form.querySelectorAll("main > div"));
	ldivs.pop();
	ldivs.forEach(function(div) {
	    div.style.opacity = 1.0;
	});
	if(div && div.hasAttribute("data-result")) {
	    const results = div.parentElement.querySelectorAll("input:checked");
	    main.querySelectorAll("input").forEach(inp => inp.checked= false);
	    if(results.length == 0) {
		form.querySelectorAll('[data-row]').forEach(function(row) {
                    row.style.display="none";
		});
		return update_stats();
	    }
	    /* This is clicking on outcome be wary */
	    topalert("When filtering by Outcome the Decision Point values can look confounded!","warn",4);
	    ldivs.forEach(function(div) {
		div.style.opacity = 0.6;
	    });
	    let counter = 0;
	    ssvcTable.forEach(function(mrow,i) {
		let row = simpleCopy(mrow);
		let drows = form.querySelectorAll("[data-row]");
		drows[i].style.display = "none";
		results.forEach(function(result) {
		    result.checked = true;
		    result.parentElement.style.opacity = 1.0;
		    if(row[result.name] == result.value) {
			counter++;
			drows[i].style.display = "table-row";
			delete row[result.name];
			Object.entries(row).forEach(function([dpname,dpvalue]) {
			    let sel = 'input[name="'+dpname +
				'"][value="'+dpvalue+'"]';
			    let inp = form.querySelector(sel);
			    if(inp)
				inp.checked = true;
			});
		    }
		});
	    });
	    const h5 = form.querySelector("h5");
            let text = String(counter) + " of " + String(ssvcTable.length)
            h5.innerText = "-- SSVC Table (selected " + text + ") -- ";
	    return update_stats();
	}
	if(ev.target && ev.target.tagName.toUpperCase() == "INPUT"
	   && ev.target.type.toLowerCase() == "checkbox") {
	    graphModule.graph_dynamic(ev.target);
	}
	main.querySelectorAll("[data-result]").forEach(function(result) {
	    result.style.fontWeight = "normal";
	    result.style.opacity = "0.6";
	    const inp = result.querySelector("input");
	    if(inp)
		inp.checked = false;
	});
	const selections = {};
	main.querySelectorAll("input:checked").forEach(function(input) {
	    const div = input.parentElement;
	    /*Ignoore outcome checkboxes that are checked */
	    if(div && div.hasAttribute("data-result"))
		return;
	    if(input.name in selections)
		selections[input.name].push(input.value);
	    else
		selections[input.name] = [input.value];
	});
	let rows = ssvcTable;
	Object.keys(selections).forEach(function(decision_point) {
	    const dp = get_decision_point(decision_point);
	    exporter.ssvcV1_0_1.selections.push({"namespace": dp.namespace || "ssvc",
						 "version": dp.version || "1.0.0",
						 "values": selections[decision_point],
						 "name": decision_point});
	    let chosen = selections[decision_point];
	    rows = rows.filter(function(row) {
		if(chosen.includes(row[decision_point])){
		    if(outcomeTitle in row) {
			return row;
		    }
		}
	    });
	});
	form.querySelectorAll("[data-row]").forEach(function(trow) {
	    trow.style.display = "none";
	});
	rows.forEach(function(row) {
	    form.querySelectorAll("[data-row]").forEach(function(trow) {
		let crow = JSON.parse(trow.getAttribute("data-row"));
		if(compareObj(crow,row))
		    trow.style.display = "table-row";
	    });
	    const rowTitle = row[outcomeTitle].replaceAll('"','\\"');
	    main.querySelectorAll('[data-result="'+rowTitle+'"]').forEach(function(result) {
		result.style.fontWeight = "bolder";
		result.style.opacity = "1.0";
		const inp = result.querySelector("input");
		if(inp)
		    inp.checked = true;
	    });
	});
	const h5 = form.querySelector("h5");
	let text = String(rows.length) + " of " + String(ssvcTable.length)
	h5.innerText = "-- SSVC Table (selected " + text + ") -- ";
	exporter.ssvcV1_0_1.timestamp =  (new Date()).toISOString();
	/* always display JSON Tree
	   code.innerHTML = JSON.stringify(exporter, null, 4);
	*/
	update_stats();
    }
    main.addEventListener('change', filterData);
    update_stats();
}


function calculateEntropy(decision_table, targetCol) {
  const valueCounts = {};
  decision_table.forEach(row => {
    const value = row[targetCol];
    valueCounts[value] = (valueCounts[value] || 0) + 1;
  });

  const totalCount = decision_table.length;
  let entropy = 0;
  for (const count of Object.values(valueCounts)) {
    const p = count / totalCount;
    entropy -= p * Math.log2(p);
  }
  return entropy;
}

function calculateInformationGain(decision_table,featureCol, targetCol) {
    const totalEntropy = calculateEntropy(decision_table, targetCol);
    const featureSet = new Set(decision_table.map(row => row[featureCol]));
    const featureValues = Array.from(featureSet);

  let weightedEntropy = 0;
  featureValues.forEach(value => {
      const subset = decision_table.filter(row => row[featureCol] === value);
      const subsetEntropy = calculateEntropy(subset, targetCol);
      const subsetWeight = subset.length / decision_table.length;
      weightedEntropy += subsetWeight * subsetEntropy;
  });

  return totalEntropy - weightedEntropy;
}

/* const entropyMain = calculateEntropy(decision_table, outcome); */
/* calculateInformationGain(decision_table, decision_point, outcome); */

function loadSSVC(fileurl) {
    form.innerHTML = "";
    if(fileurl == "upload_file") {
	form.parentElement.querySelector("input[type='file']").click();
	return;
    }
    if(fileurl.indexOf("csv:") == 0) {
	/* fileurl itself is the payload with csv: in the front*/
	return createSSVC(fileurl.substring(4)); 
    }
    if(fileurl.indexOf("json:") == 0) {
	/* fileurl itself is the payload with json: in the front*/
	return createSSVC(JSON.parse(fileurl.substring(5))); 
    }
    if(fileurl.match(/^\d+$/)) {
	const index = parseInt(fileurl);
	if( index in decision_trees && decision_trees[index].data) {
	    /* This is a decision_point index find it and return */
	    return createSSVC(decision_trees[index].data);
	}
    }
    fetch(fileurl).then(function(d) {
	d.text().then(function(csv) {
	    try {
		const json = JSON.parse(csv);
		createSSVC(json);
	    }catch(err) {
		console.log("Assuming the uplaoded document is CSV");
		createSSVC(csv);
	    }
	});
    });
}
async function get_decision_points() {
    /* Use the URL registry = await response.json(); */
    const registry_url = "https://raw.githubusercontent.com/CERTCC/SSVC/refs/heads/main/data/json/ssvc_object_registry.json";
    const response = await fetch(registry_url);
    const registry = await response.json();
    if (registry.types && registry.types.DecisionPoint &&
	registry.types.DecisionPoint.namespaces) {
	const namespaces = registry.types.DecisionPoint.namespaces;
	for (const nsKey in namespaces) {
	    const namespace = namespaces[nsKey];
	    if (namespace.keys) {
		for (const key in namespace.keys) {
		    const keyEntry = namespace.keys[key];
		    if (keyEntry.versions) {
			for (const version in keyEntry.versions) {
			    const versionEntry = keyEntry.versions[version];
			    if (versionEntry.obj && versionEntry.values) {
				let mdata = {data: versionEntry.obj};
				decision_points.push(mdata);
			    }
			}
		    }
		}
	    }
	}
    }
    if (registry.types && registry.types.DecisionTable &&
	registry.types.DecisionTable.namespaces) {
	const namespaces = registry.types.DecisionTable.namespaces;
	for (const nsKey in namespaces) {
	    const namespace = namespaces[nsKey];
	    if (namespace.keys) {
		for (const key in namespace.keys) {
		    const keyEntry = namespace.keys[key];
		    if (keyEntry.versions) {
			for (const version in keyEntry.versions) {
			    const versionEntry = keyEntry.versions[version];
			    if (versionEntry.obj && versionEntry.obj.decision_points) {
				let mdata = {data: versionEntry.obj, displayname: name_version(versionEntry.obj)};
				if(versionEntry.obj.name.indexOf("Deployer") > -1)
				    mdata['selected'] = true;
				decision_trees.push(mdata);
			    }
			}
		    }
		}
	    }
	}
    }    
    decision_points.sort(dtreeSort);
    load_trees();
}

function deepSet(form, obj, path) {
    if(!path)
	path = "";
    for (const key in obj) {
	if (typeof obj[key] === "object") {
	    deepSet(form, obj[key], path ? path + "-" + key : key);
	} else {
	    const fullpath = path ? path + "-" + key : key;
	    const input = form.elements.namedItem("obj-" + fullpath);
	    if(input) {
		input.value = obj[key];
		input.defaultValue = obj[key];
		if(input.onchange)
		    input.onchange(input);
	    } else {
		console.log("Unassigned value ", key, fullpath, obj[key]);
	    }
	}
    }
}
function match_name_ns_vers(obj,selectobj) {
    const props = ["name", "namespace", "version"];
    return props.every(function(prop) {
	return obj.data.hasOwnProperty(prop) &&
	    selectobj.hasOwnProperty(prop) &&
	    obj.data[prop] == selectobj[prop];
    });
}
function prepare_form(vForm, vSelect, selectdp, preFill, vars) {
    if(!vSelect.hasAttribute("detect-change"))
       vSelect.addEventListener("change",function(ev) {
	   const el = ev.target;
	   if(!el.value)
	       return clear_popup_form(vSelect, vForm);
	   const obj = JSON.parse(el.value);
	   Object.keys(obj).forEach(function(key) {
	       vForm.querySelectorAll("[data-temp]").forEach(function(div) {
		   div.remove();
	       });
	       if(vars in obj) {
		   const drows = obj[vars].length * 2;
		   const crows = vForm.querySelectorAll("[data-clone]").length;
		   const diff = (drows - crows)/2;
		   for(let i=0; i < diff; i++)
		       vForm.querySelector("button").click();
	       }
	       deepSet(vForm, obj);
	   });
       }); 
    vSelect.setAttribute("detect-change","1");
    preFill.forEach(function(obj) {
	let info;
	/* Drop down for decision points has more information*/
	if (obj.data.namespace && obj.data.name && obj.data.version) 
	    info = obj.data.namespace + "/" + name_version(obj.data);
	else
	    info = obj.data.name;
	const opt = new Option(info, JSON.stringify(obj.data));
	if(selectdp.name  && match_name_ns_vers(obj,selectdp)) {
	    opt.selected = true;
	    selectdp['obj'] = true; 
	}
	vSelect.appendChild(opt);
    });
    if(selectdp.obj) {
	vSelect.dispatchEvent(new Event("change"));
    }
}
function popupStart(selector) {
    const popup = form.parentElement.parentElement.querySelector("[id='ssvcPopup']"); 
    form.style.opacity = "0.3";
    form.style.pointerEvents = "none";
    popup.style.display = "block";
    /* The matching div under popup to display and work with */
    let rpopup;
    Array.from(popup.children).forEach(function(el) {
	if(el.hasAttribute(selector)) {
	    el.style.display = "block";
	    rpopup = el;
	} else {
	    el.style.display = "none";
	}
    });
    return rpopup;
}
function popupEnd() {
    const popUp = form.parentElement.parentElement.querySelector("[id='ssvcPopup']");
    form.style.opacity = "1.0";
    form.style.pointerEvents = "all";
    popUp.style.display = "none";
    return popUp;
}

async function popupConfirm(message) {
    const rpopUp = popupStart("data-yesno");
    rpopUp.querySelector("h4").innerText = message;
    return new Promise(function(success, fail ) {
	rpopUp.querySelectorAll("button").forEach(function(el) {
	    el.onclick = function() { success(el.innerText); popupEnd();}
	});
	
    });
}
function clear_popup_form(iSelect, rpopUp) {
    iSelect.selectedIndex = 0;
    rpopUp.querySelectorAll("[data-temp]").forEach(function(el) {
	el.remove();
    });
    rpopUp.querySelectorAll("input,textarea").forEach(function(input) {
	input.value="";
    });
}

function disable_current_dps(options) {
    /* Disable already used DPs */
    const current_dps = [];
    form.querySelector("main").querySelectorAll("[data-dp]").forEach(function(el) {
	try {
	    const dp = get_decision_point(el.getAttribute("data-dp"));
	    current_dps.push(dp);
	} catch(err) {
	    console.log("Error while trying to detect current Decision Points " + err);
	}
    });
    options.forEach(function(option) {
	if(option.value && (!option.selected)) {
	    try {
		const odp = JSON.parse(option.value);
		current_dps.forEach(function(cdp) {
		    if(match_name_ns_vers({"data": odp},cdp))
			option.setAttribute("disabled",1);
		});
	    } catch(err) {
		console.log("Error while trying to match Decision Points to current options" + err);
	    }
	}
    });
}

function popupEditDP(w) {
    topalert();
    const rpopUp = popupStart("data-customdp");
    const dpForm = rpopUp.querySelector("form");
    const dpSelect = dpForm.querySelector("select");
    let options = dpSelect.querySelectorAll("option");
    let dpName = "-1";
    let dpIndex = "-1";
    options.forEach(function(option) {
	if(option.getAttribute("disabled"))
	    option.removeAttribute("disabled");
    });
    if(options.length < 2) {
	/*First time popup is running for Decision Points */
	prepare_form(dpForm, dpSelect, {}, decision_points, "values");
	options = dpSelect.querySelectorAll("option");
    } else if(decision_points.length > options.length - 1) {
	/* Add any new Decision Points that were imported or added */
	for(let i=options.length - 1; i < decision_points.length; i++) {
	    const obj = decision_points[i];
	    const info = obj.data.namespace + "/" + name_version(obj.data);
	    const opt = new Option(info, JSON.stringify(obj.data));
	    dpSelect.appendChild(opt);
	}
	options = dpSelect.querySelectorAll("option");	
    }

    if(w.parentElement.hasAttribute("data-outcomeName")) {
	dpSelect.setAttribute("data-outcomeName",
			      w.parentElement.getAttribute("data-outcomeName"));
	rpopUp.querySelector("h4").innerHTML = "Customize Outcome";	
	
    } else if(w.hasAttribute("data-adddp")) {
	dpSelect.removeAttribute("data-outcomeName");
	/* This is a new Decision Point so Add Decision Point is the action */
	rpopUp.querySelector("h4").innerHTML = "Add Decision Point";
	rpopUp.querySelector("[data-update]").innerText = "Add";
    } else {
	dpSelect.removeAttribute("data-outcomeName");
	rpopUp.querySelector("h4").innerHTML = "Customize Decision Point";
	rpopUp.querySelector("[data-update]").innerText = "Update";	
	dpName = w.parentElement.getAttribute("data-dp");
	dpIndex = w.parentElement.getAttribute("data-dpIndex");
	const selectdp = get_decision_point(dpName);
	if(selectdp.name) {
	    dpSelect.setAttribute("data-selectdp", JSON.stringify(selectdp));
	    const i = decision_points.findIndex(function(dp) {
		return match_name_ns_vers(dp,selectdp);
	    });
	    if (i > -1) {
		dpSelect.options.selectedIndex = i + 1;
		dpSelect.dispatchEvent(new Event("change"));
	    }
	} else {
	    /* This decision point is unknown to us */
	    dpSelect.removeAttribute("data-selectdp");
	    clear_popup_form(dpSelect, rpopUp);
	}
    }
    
    dpForm.setAttribute("data-dpIndex", dpIndex);
    dpForm.setAttribute("data-dp", dpName);
    disable_current_dps(options);
}
function toggleAll(doselect) {
    const main = form.querySelector('main');
    if (arguments.length < 1) {
	const selected = main.querySelectorAll('input[type="checkbox"]:not(:checked)').length;
	if (selected)
	    doselect = true;
	else
	    doselect = false;
    }
    let tempel;
    main.querySelectorAll("input[type='checkbox']").forEach(function(el) {
	el.checked = doselect;
	tempel = el;
    });
    main.dispatchEvent(new Event('change'));
    /* Put full tree back like it was */
    try {
	const jsonData = document.querySelector("[data-tab='JSON']").innerText;
	const jsonTree = JSON.parse(jsonData);
	graphModule.dt_graph(jsonTree);
    } catch(err) {
	console.log("Reset form error " + err);
    }
}
function selectCustom(name, datatree, fIndex) {
    let clbutton = form.parentElement.querySelector("[data-clear]");
    clbutton.setAttribute("data-json", JSON.stringify(datatree, null, 2));
    const sample = form.parentElement.querySelector("[id='sampletrees']");
    if(sample.querySelector("[selected]"))
	sample.querySelector("[selected]").removeAttribute("selected");
    if(fIndex < 0) {
	const opt = new Option(name, String(fIndex * -1), false, true);
	if(name) {
	    opt.text = "[Private] " + name
	    opt.selected = true;
	    opt.setAttribute("data-customdt",1);
	}
	sample.appendChild(opt);
    } else {
	sample.querySelectorAll("option").forEach(function(option) {
	    if(option.textContent == name) 
		option.value = fIndex;
	});
    }
    toggleAll(true);
}
function verify_update_mapping(inp, clbutton) {
    let val = inp.value;
    let jsonTree = JSON.parse(clbutton.getAttribute("data-json"));
    if(jsonTree && jsonTree.mapping) {
	let outcomedp = jsonTree.decision_points[jsonTree.outcome];
	let dpv = outcomedp.values.find(dpv => dpv.name == val);
	if(!dpv) {
	    alert("The Outcome is not part of the planned Outcomes");
	    return false;
	}
	let index = -1;
	form.querySelectorAll("input[data-initialvalue]")
	    .forEach(function(cinp,i) {
		if(cinp == inp)
		    index = i;
	    });
	if(index < 0) {
	    alert("Unable to find matching row in mapping");
	    return false;
	}
	jsonTree.mapping[index][jsonTree.outcome] = dpv.key;
	clbutton.setAttribute("data-json",JSON.stringify(jsonTree));
	return true;
    } else {
	alert("Unable to update new Outcome");
	return false;
    }
}
function customize(w) {
    const clbutton = form.parentElement.querySelector("[data-clear]");
    if(w.innerHTML == "Customize") {
	clbutton.removeAttribute("data-changed");
	topalert("Edit, Remove or Add Decision Points, update Outcomes to create a new Decision Model and save it as a Decision Tree","success",0);
	toggleAll(true);
	w.innerHTML = "Save Changes";
	lock_unlock(true);
	form.querySelectorAll("input[type='checkbox']").forEach(function(checkbox) {
	    checkbox.disabled = true;
	    checkbox.nextSibling.style.opacity = 0.5;
	});
	const divOutcome = form.querySelector("[data-outcomeName]");
	const span = document.createElement("span");
	span.innerHTML = "&#9998;";
	span.style.color = "#007bff";
	span.addEventListener("click",function() {
	    popupEditDP(this);
	});
	divOutcome.appendChild(span);
	const alldps = form.querySelectorAll("[data-dp]");
	/* There are two displays of each DP*/
	const dplength = alldps.length/2;
	alldps.forEach(function(el, i) {
	    if(el.querySelector("span"))
		return;
	    const span = document.createElement("span");
	    span.innerHTML = "&#9998;";
	    span.style.color = "#007bff";
	    span.title = "Edit Decision Point";
	    span.addEventListener("click",function() {
		popupEditDP(this);
	    });
	    const delspan = document.createElement("span");
	    delspan.title = "Delete Decision Point";
	    delspan.innerHTML = "&#8854;";
	    delspan.addEventListener("click", function(ev) {
		deleteDP(this);
	    });
	    delspan.style.color = "red";
	    el.appendChild(span);
	    if(!((i == dplength -1) || (i == dplength*2 -1)))
		el.appendChild(delspan);
	    el.setAttribute("TM",String(i) + "- " + String(dplength));
	    if((i == dplength - 2) || (i == dplength*2 - 2)) {
		const addspan = document.createElement("span");
		addspan.innerHTML = "&#8853";
		addspan.style.color = "#28a745";
		addspan.setAttribute("data-adddp",1);
		addspan.addEventListener("click", function(ev) {
		    popupEditDP(this);
		});
		el.appendChild(addspan);
	    }
	});
	form.querySelectorAll("[data-outcome]").forEach(function(el) {
	    const inp = document.createElement("input");
	    inp.value = el.innerText;
	    inp.dataset.initialvalue = el.innerText;
	    inp.addEventListener('change', function(e) {
		const inp = e.target;
		inp.style.border = "1px solid grey";
		if(!inp.value)
		    return alert("Outcome cannot be empty!");
		if (inp.value !== inp.dataset.initialValue) {
		    if(verify_update_mapping(inp,clbutton)) {
			clbutton.setAttribute("data-changed", "1");
		    } else {
			inp.style.border = "2px solid red";
			inp.focus();
		    }
		}
	    });
	    el.innerText = "";
	    el.appendChild(inp);
	});
    } else {
	/* new Decision Tree Setup  */
	if(!clbutton.hasAttribute("data-changed")) {
	    return alert("Nothing has changed or error field not fixed!");
	}
	let jsonTree = {};
	if(clbutton.hasAttribute("data-json")) {
	    jsonTree = JSON.parse(clbutton.getAttribute("data-json"));
	}
	/* Do we need to update mapping?*/
	const sample = form.parentElement.querySelector("[id='sampletrees']");
	const nextel = sample.nextElementSibling;
	let current = sample[sample.selectedIndex].innerText
	if(nextel.tagName.toUpperCase() == "DIV") {
	    nextel.querySelectorAll("input").forEach(function(inp) {
		if(!inp.value) 
		    jsonTree["error"] = "Value for " + niceString(inp.name) 
		    + " CANNOT be empty!";
		jsonTree[inp.name] = inp.value;
	    });
	}
	if(jsonTree.error)
	    return alert(jsonTree.error);
	if(!validate_namespace(jsonTree.namespace)) 
	    return;
	w.innerHTML = "Customize";
	lock_unlock(false);
	form.querySelectorAll("input[type='checkbox']").forEach(function(checkbox) {
	    checkbox.disabled = false;
	    checkbox.nextSibling.style.opacity = 1.0;
	});
	/* Update JSON Tree Mapping */
	form.querySelectorAll("[data-dp]").forEach(function(el) {
	    if(el.querySelector("span"))
		el.querySelector("span").remove();
	});
	form.innerHTML = "";
	createSSVC(jsonTree, false);
	/* Find if this is already a custom built tree and
	   update it if needed */
	let findex = decision_trees.findIndex(function(dt) {
	    if(dt.custom)
		return dt.displayname == current;
	    else 
		current = name_version(jsonTree);
	});
	
	topalert("Latest values have been saved locally!","success",3);
	if(findex > -1) {
	    decision_trees[findex]["data"] = jsonTree;
	} else {
	    /* Now findex will basicaly represent the last element
	       in the decision_trees */
	    findex = -1 * decision_trees.length;
	    decision_trees.push({data: jsonTree, displayname: current, custom: 1});
	}
	selectCustom(current, jsonTree, findex);
	let custom_ssvc = {};
	["decision_trees","decision_points"].forEach(function(dtype) {
	    custom_ssvc[dtype] = [];
	    SSVC[dtype].forEach(function(dtdp) {
		if(dtdp.custom)
		    custom_ssvc[dtype].push(dtdp);
	    });
	})
	localStorage.setItem("custom_ssvc", JSON.stringify(custom_ssvc));
	form.parentElement.querySelector("[data-session]").style.display = "block";
    }
}
function load_trees() {
    if(!form)
	return;
    const sampletrees = form.parentElement.querySelector("[id='sampletrees']");
    sampletrees.innerHTML = "";
    const displaySet = {};
    decision_trees.forEach(function(decision_tree, i) {
	const opt = new Option(decision_tree.displayname, i , decision_tree.selected, decision_tree.selected);
	if(decision_tree.custom) {
	    opt.setAttribute("data-customdt","1");
	    opt.innerText =  "[Private] " +opt.innerText
	}
	if(displaySet[opt.innerText])
	    opt.innerText = add_dash_n(opt.innerText, displaySet);
	sampletrees.appendChild(opt);
	if(decision_tree.selected)
	    loadSSVC(String(i));
	displaySet[opt.innerText] = 1;
    });
    sampletrees.appendChild(new Option("Upload CSV/JSON","upload_file"));
}
async function delete_session() {
    if(await popupConfirm("Are you sure, you want to delete all custom Decision Trees?") == "Yes") {
	localStorage.removeItem("custom_ssvc");
	for (let i = 0; i < decision_trees.length; i++) {
	    if(decision_trees[i].custom) {
		decision_trees.splice(i, 1);
		i--; 
	    }
	}
	topalert("All custom decision trees have been removed", "warn");
	load_trees();
	form.parentElement.querySelector("[data-session]").style.display = "none";	
    } else {
	topalert("Good! Custom decision trees have been retained!", "success", 3);
    }
}
async function delete_dtree() {
    const sampletrees = form.parentElement.querySelector("[id='sampletrees']");
    const delete_tree = sampletrees.options[sampletrees.selectedIndex].innerText;
    const opt = sampletrees.options[sampletrees.selectedIndex];
    if(!opt.hasAttribute("data-customdt")) {
	return alert("The default trees cannot be deleted");
    }
    if(await popupConfirm("Are you sure, you want to delete custom Decision Tree \""+ delete_tree  + "\"?") == "Yes") {
	let old_tree = simpleCopy(decision_tree[parseInt(opt.value)]);
	decision_tree.splice(parseInt(opt.value), 1);
	sampletrees.options[sampletrees.selectedIndex].remove();
	sampletrees.dispatchEvent(new Event("change"));
	const saved = JSON.parse(localStorage.getItem("custom_ssvc"));
	let savedIndex = saved.decision_trees.findIndex(function(dt) {
	    return match_name_ns_vers(dt,old_tree.data);
	});
	if(savedIndex > -1)
	    saved.decision_trees.splice(savedIndex,1);
	localStorage.setItem("custom_ssvc", JSON.stringify(saved));
    } else {
	topalert("Good! Nothing was deleted!", "success", 3);
    }
}
function rename_dtree() {
    const sampletrees = form.parentElement.querySelector("[id='sampletrees']");
    const opt = sampletrees.options[sampletrees.selectedIndex];
    if(!opt.hasAttribute("data-customdt")) {
        alert("The default trees cannot be deleted");
	return;
    }
    const old_index = parseInt(sampletrees.options[sampletrees.selectedIndex].value);
    if(decision_trees[old_index] && decision_trees[old_index].data) {
	const old_tree = decision_trees[old_index];
	const old_name = old_tree.data.name;
	const new_name = prompt("Enter new name for the current decision tree \"" + old_name + "\":");
	decision_trees[old_index].data.name = new_name;
	opt.innerText = name_version(decision_trees[old_index].data);
	decision_trees[old_index].displayname = opt.innerText;
	const saved = JSON.parse(localStorage.getItem("custom_ssvc"));
        let savedIndex = saved.decision_trees.findIndex(function(dt) {
            return match_name_ns_vers(dt,old_tree.data);
	});
        if(savedIndex > -1)
            saved.decision_trees[savedIndex] = decision_trees[old_index];
	localStorage.setItem("custom_ssvc", JSON.stringify(saved));
    }
}
function download_ssvc_csv() {
    download_ssvc('csv');
}
function download_ssvc_json() {
    download_ssvc('json');
}
function download_ssvc(dtype) {
    const btn = form.parentElement.querySelector("[data-download-" + dtype + "]");
    btn.click();
}
function restore_session() {
    if(localStorage.getItem("custom_ssvc")) {
	const saved = JSON.parse(localStorage.getItem("custom_ssvc"));
	delete saved.form;
	["decision_points","decision_trees"].forEach(function(item) {
	    console.log(saved[item]);
	    SSVC[item].push.apply(SSVC[item],saved[item]);
	});
	load_trees();
	topalert("Session variables have been restored!","success",3);
    } else {
	topalert("No previous session has been found to restore!","danger");
    }
}
    function ssvc_launch() {
	form = document.getElementById('ssvcForm');
	if(decision_trees.length < 1) 
	    get_decision_points();
	else
	    load_trees();
	if(form && localStorage.getItem("custom_ssvc")) {
	    topalert("You have some custom Decision Trees saved from earlier session. " +
		     "use \"Restore Session\" under \"Custom Trees\" to restore & manage these",
		     "success",0);
	    form.parentElement.querySelector("[data-session]").style.display = "block";
	}
    }
    document$.subscribe(function() {
	ssvc_launch();
    });
function dpValueClone(el) {
    const pDiv = el.parentElement.parentElement;
    pDiv.querySelectorAll("span").forEach(function(x) { x.remove(); });
    const count = pDiv.querySelectorAll("[data-clone]").length/2 - 1;
    const delspan = document.createElement("span");
    delspan.innerHTML = "&#8854;";
    delspan.addEventListener("click", function(ev) {
	const el = this;
	el.parentElement.parentElement.nextSibling.remove();
	el.parentElement.parentElement.remove();
    });
    delspan.style.color = "red";
    [el.parentElement.nextElementSibling,
     el.parentElement.nextElementSibling.nextElementSibling].forEach(function(row,i) {
	 const nrow = row.cloneNode(true);
	 const nel = nrow.querySelector("input,textarea");
	 nel.value = "";
	 if(nel.onchange)
	     nel.onchange(nel);
	 nel.name = nel.name.replace(/(\d+)([^\d]*)$/, function(_,n,g) {
	     return String(count + 1)+g
	 });
	 nrow.setAttribute("data-temp","1");
	 if (i == 0)
	     nrow.children[0].prepend(delspan);
	 pDiv.appendChild(nrow);
     });
}

function textAreaAutoSize(element) {
    element.style.height = "1px";
    element.style.height = String(4 + element.scrollHeight) + "px";
}
function set_deep(obj,prop,val) {
    /* For the Object obj set the property of a prop to val
       recursively. example set_deep({a:{b:{c:{"good"}}}},"a-b-c","bad")
       will return {a:{b:{c:{"bad"}}}} */
    if(typeof(obj) != "object")
	return undefined;
    let fobj = simpleCopy(obj);
    var x = fobj;
    let props = prop.split("-");
    let fprop = props.pop();
    for(var i=0; i<props.length; i++) {
	if(props[i] in x) {
	    x = x[props[i]];
	    continue;
	} else {
	    if(i+1 < props.length) {
		if (props[i+1].match(/^\d+$/))
		    x[props[i]] = [];
		else
		    x[props[i]] = {};
	    } else if (fprop.match(/^\d+$/))  {
		/* Last element and is an array */
		x[props[i]] = [];
	    } else {
		x[props[i]] = {};
	    }
	    x = x[props[i]];
	}
    }
    /* If the value is being set to be undefined then delete this property
       of this object */
    if(val === undefined) {
	if (fprop.match(/^\d+$/)) {
	    x.splice(parseInt(fprop),1);
	} else {
	    delete x[fprop];
	}
    } else {
	x[fprop] = val;
    }
    return fobj;
}
function deepGet(inputs) {
    let fdp = {};
    inputs.forEach(function(input) {
	fdp = set_deep(fdp,input.name,input.value);
    });
    if(fdp.obj)
	return fdp.obj;
    return {};
}
function makeTree(jsonTree) {
    const clbutton = form.parentElement.querySelector("[data-clear]");    
    jsonTree.mapping = [];
    jsonTree.mapping = enumerateCombinations(jsonTree);
    form.innerHTML = "";
    jsonTree.key = uniq_key(jsonTree, decision_trees.map(x => x.data),"DT_", 2);
    console.log(jsonTree);
    createSSVC(jsonTree, false);
    customize({innerHTML: "Customize"});
    clbutton.setAttribute("data-changed","1");
    topalert();
    topalert("New Decision Tree has Outcomes that are evenly laid out! Please update these " +
	     "as appropriate for your Decision Model, before Saving it!","warn",0);
}
async function deleteDP(el) {
    const dpName = el.parentElement.childNodes[0].textContent;
    const confirm = await popupConfirm('Do you want to delete Decision Point "' + dpName + '"');
    if(confirm == "Yes") {
	try { 
	    const delDP = el.parentElement.getAttribute("data-dp");
	    const alldps = Array.from(form.querySelectorAll("main [data-dp]")).map(function(el) { return el.getAttribute("data-dp")});
	    if(alldps.length < 3) {
		topalert("Minimum two decision points are needed", "danger");
		return false;
	    }
	    const removedp = JSON.parse(el.parentElement.parentElement.getAttribute("data-help"));
	    console.log(removedp);
	    const clbutton = form.parentElement.querySelector("[data-clear]");
	    const jsonTree =  JSON.parse(clbutton.getAttribute("data-json"));
	    const matched = Object.keys(jsonTree.decision_points).some(function(dpkey) {
		const dp = jsonTree.decision_points[dpkey];
		if(match_name_ns_vers({data: dp},removedp)) {
		    delete jsonTree.decision_points[dpkey];
		    return true;
		}
		return false;
	    });
	    if(matched)
		makeTree(jsonTree);
	    else
		throw "Could not delete decision point"; 
	} catch(err) {
	    topalert(err,"danger");
	}
    }
}
function find_key(dp,dt) {
    /* Find a decision points' key attribute in a decision tree*/
    if('decision_points' in dt) {
	for (const [fkey, fdp] of Object.entries(dt.decision_points)) {
	    if(['name','namespace','version'].every(function(prop) {
		return prop in fdp && prop in dp && dp[prop] == fdp[prop];
	    }))
		return fkey;
	}
    }
    return; 
}
function uniq_key(obj, arr, prefix, copyLength) {
    if(!prefix)
	prefix = "";
    if(copyLength && String(copyLength).match(/^[0-9]$/)) {
	copyLength = parseInt(copyLength);
    } else {
	copyLength = 1;
    }
    let base = obj.name.normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-zA-Z0-9_]/g, "")
        .toUpperCase();

    if (copyLength && copyLength > 0) {
        base = base.substring(0, copyLength);
    }

    if (!base[0] || !/[A-Z0-9]/.test(base[0])) {
        base = "A" + base; 
    }

    if (base.length === 0) {
        base = "A";
    }

    let xkey = prefix + base;
    let counter = 0;

    while (arr.findIndex(xdp => xdp.key === xkey) > -1) {
        counter++;
        xkey = prefix + base + "_" + counter;
    }

    return xkey;
}

function validate_namespace(namespace) {
    if(!namespace.toLowerCase().startsWith("x_")) {
	/* Only thing allowed is translation  */
	if(!namespace.match(/\/[a-z\-0-9]*\//i)) {
	    alert("Changed Decision Point or Tree Namespace cannot use reserved namespaces. Either use x_com.example#psirt format or a pure translation ssvc/de-DE/ is allowed.");
	    return false;
	}
    }
    return true;
}
function enumerateCombinations(dtree) {
    const decisionPoints = dtree.decision_points;
    const outcomeKey = dtree.outcome;

    const relevantPoints = Object.entries(decisionPoints)
	  .filter(([key]) => key !== outcomeKey);

    const pointsWithValues = relevantPoints.map(([id, dp]) => ({
	id: id,
	values: dp.values.map(v => v.key)
    }));

    function cartesianProduct(index, current, result) {
	if (index === pointsWithValues.length) {
	    current[outcomeKey] = "0";
	    result.push(Object.assign({}, current));
	    return;
	}

	const point = pointsWithValues[index];
	Array.from(point.values).forEach(function (value) {
	    current[point.id] = value;
	    cartesianProduct(index + 1, current, result);
	});
    }

    const result = [];
    cartesianProduct(0, {}, result);

    const outcomeValues = decisionPoints[outcomeKey].values.map(v => v.key);
    const outcomeCount = outcomeValues.length;
    /* Spread outcome evenly across the results array*/
    const m = result.length;
    const n = outcomeValues.length;
    const blockSize = Math.floor(m / n);
    let remainder = m % n;
    
    let index = 0;
    for (let i = 0; i < n; i++) {
	let size = blockSize + (remainder > 0 ? 1 : 0);
	remainder = Math.max(0, remainder - 1);
	
	for (let j = 0; j < size; j++) {
	    result[index][outcomeKey] = outcomeValues[i];
	    index++;
	}
    }
    return result;
}


function updateTree() {
    const clbutton = form.parentElement.querySelector("[data-clear]");
    clbutton.removeAttribute("data-changed")
    let jsonTree = {};
    if(clbutton.hasAttribute("data-json")) {
	jsonTree = JSON.parse(clbutton.getAttribute("data-json"));
    }
    const popUp = form.parentElement.parentElement.querySelector("[id='ssvcPopup']");
    const updatebtn = popUp.querySelector("[data-update]");    
    const dpForm = popUp.querySelector("[data-customdp]")
	  .querySelector("form");
    const dpSelect = dpForm.querySelector("select");
    const dpOutcome = dpSelect.getAttribute("data-outcomeName");
    let changed = false;
    const inputs = dpForm.querySelectorAll("input,textarea");
    let dp = deepGet(inputs);
    for(let i=0; i<inputs.length; i++) {
	if(inputs[i].type == "checkbox") continue;
	if(inputs[i].value == "") {
	    topalert("All input fields are required for a Decision Point",
		     "danger");
	    return;
	}
	if(inputs[i].defaultValue && inputs[i].defaultValue != inputs[i].value) {
	    changed = true;
	    break;
	}
    }
    let olddp = {};
    /* Get previous decision point so we can compare it to the current */
    if(dpSelect.hasAttribute("data-selectdp")) 
	olddp = JSON.parse(dpSelect
			   .getAttribute("data-selectdp"));
    /*Check if this decision point is in our registry */
    let registered = decision_points.some(function(x) {
	if(match_name_ns_vers(x, dp)) {
	    dp = x.data;
	    return true;
	}
    });
    
    if(changed) {
	/*Check if it is a translation. */
	if(!validate_namespace(dp.namespace)) {
	    return;
	}
	/* Add data to dpMap and decision_points of global SSVC data */
	dpMap[dp.name] = {"namespace": dp.namespace, "version": dp.version};
    } else  {
	if(match_name_ns_vers({"data": dp}, olddp)) {
	    alert("Nothing has changed");
	    return;
	}
    }
    let dpvkeys = {}
    /* Doube verify and make sure tke key uniqueness */
    dp.values.forEach(function(val,i) {
	if(!dp.values[i].key)
	    dp.values[i].key = uniq_key(val, dp.values);
	if(dp.values[i].key in dpvkeys)
	    dp.values[i].key = uniq_key(val, dp.values);
	dpvkeys[dp.values[i].key] = 1;
    });
    popupEnd();
    let oldKey = find_key(olddp,jsonTree);
    if(!registered) {
	/* Enforce unique keys for values*/
	dp.key = uniq_key(dp, decision_points.map(x => x.data));
	const info = dp.namespace + "/" + name_version(dp);
	let opt = Array.from(dpSelect.querySelectorAll("option"))
	    .filter(function(x) {
		return x.innerText == info
	    });
	if(opt.length) {
	    opt[0].value = JSON.stringify(dp);
	} else {
	    opt = new Option(info, JSON.stringify(dp));
	    dpSelect.appendChild(opt);
	}
	decision_points.push({"filename": "memory:" + dp.namespace
				   + dp.name, "data": dp, custom: 1});	
    }
    if(oldKey) {
	/* This is to replace a decision point */
	const oldvalues = simpleCopy(jsonTree.decision_points[oldKey].values);
	delete jsonTree.decision_points[oldKey];
	let newKey = dp.namespace + ":" + dp.key + ":" + dp.version;
	if(dp.namespace.indexOf("x_") > -1)
	    newKey = dp.namespace.substr(0,3) + ":" + dp.key + ":" + dp.version;
	jsonTree.decision_points[newKey] = dp;
	if(dpOutcome) {
	    jsonTree.outcome = newKey;
	} 
	if (olddp.values && olddp.values.length == dp.values.length) {
	    /* Leave the Tree Outcomes as-is*/
	    if(jsonTree.mapping.every(function(tmap,i) {
		let fI = oldvalues.findIndex(value => value.key == tmap[oldKey])
		if(fI > -1) {
		    delete jsonTree.mapping[i][oldKey];
		    tmap[newKey] = dp.values[fI].key;
		    return true;
		}
		return false;
	    })) {
		console.log("success");
		form.innerHTML = "";
		jsonTree.key = uniq_key(jsonTree, decision_trees.map(x => x.data),"DT_", 2);
		createSSVC(jsonTree, false);
		customize({innerHTML: "Customize"});
		clbutton.setAttribute("data-changed","1")
		return;
	    } else {
		console.log("Failed");
		console.log(jsonTree,dp);
	    }
	} 
    } else if(updatebtn.innerText == "Add") {
	if(!dp.version)
	    dp.version = "1.0.0";
	const newKey = dp.namespace + ":" + dp.key + ":" + dp.version;
	jsonTree.decision_points[newKey] = dp;
    } else {
	topalert("Error: Unable to find if this is a new Decision Point or a replacement",
		 "danger");
    }
    /* Somethings have majorly changed, we have to update the decision tree mappings */
    makeTree(jsonTree);
}
function schemaTransform(dtnew) {
    const dtobj = simpleCopy(dtnew);
    const dtold = {};
    let outcomeName;
    if('outcome' in dtobj)
	outcomeName = dtobj.outcome;
    if('decision_points' in dtobj) {
	dtold['decision_points'] = [];
	Object.entries(dtobj['decision_points']).forEach(function([k,dp]) {
	    dp.decision_type = "simple";
	    if(k == outcomeName)
		dp.decision_type = "final";
	    dp.values.forEach(function(dv) {
		dv.label = dv.name;
		delete dv.name;
	    });
	    dp.options = dp.values;
	    delete dp.values;
	    dp.label = dp.name.replaceAll(",","|");
	    delete dp.name;
	    dtold.decision_points.push(dp);
	});
    }
    if('mapping' in dtobj) {
	dtold['decisions_table'] = [];
	dtobj.mapping.forEach(function(dvpair) {
	    const dt = {}
	    Object.entries(dvpair).forEach(function([k,v]) {
		const dp = dtnew.decision_points[k];
		const name = dp.name.replaceAll(",","|");
		for(let i=0; i< dp.values.length; i++) {
		    if('key' in dp.values[i] && dp.values[i].key == v)
			dt[name] = dp.values[i].name;
		}
	    });
	    dtold['decisions_table'].push(dt);
	});
    }
    return dtold;

}
function import_json(json, name) {
    /* Convert everything to JSON 2.0.0 schema before loading */
    let outcomeName = "Priority";
    if(('schemaVersion' in json) && (json.schemaVersion == "2.0.0")) {
	if(('outcome' in json) && ('decision_points' in json) &&
	   (json.outcome in json.decision_points)) {
	    if('name' in json)
		name = json.name;
	    else
		name = "Custom Uploaded ";
	    form.innerHTML = "";
	    createSSVC(json, false);
	    /* Insert a new element in the array*/
	    let fIndex = decision_trees.findIndex(function(dtobj) {
		return match_name_ns_vers(dtobj,json);
	    });
	    if(fIndex < 0) {
		const newname = name_version(json);
		Object.values(json.decision_points).forEach(function(newdp) {
		    if(!(decision_points.some(function(dtobj) {
			return match_name_ns_vers(dtobj,newdp);
		    }))) {
			if(!newdp.version)
			    newdp.version = "1.0.0";
			decision_points.push({data: newdp});
		    }
		});
		selectCustom(newname, json, -1*(decision_trees.length));
		decision_trees.push({data:json,displayname: newname});
	    } else {
		const select = form.parentElement.querySelector("[id='sampletrees']");
		select.value = fIndex;
		select.dispatchEvent(new Event('change'));
		topalert("Imported JSON is already in the registry","warn");
	    }
	}
    } else {
	topalert("Unknown JSON file format","danger");
    }
    
}
function simpleCSV(csvString) {
    const rows = [];
    let row = [];
    let value = '';
    let inQuotes = false;

    for (let i = 0; i < csvString.length; i++) {
        const char = csvString[i];
        const nextChar = csvString[i + 1];

        if (char === '"' && inQuotes && nextChar === '"') {
            value += '"';
            i++; 
        } else if (char === '"') {
            inQuotes = !inQuotes;
        } else if (char === ',' && !inQuotes) {
            row.push(value);
            value = '';
        } else if ((char === '\n' || char === '\r') && !inQuotes) {
            if (value || row.length > 0) {
                row.push(value);
                rows.push(row);
                row = [];
                value = '';
            }
            if (char === '\r' && nextChar === '\n') i++;
        } else {
            value += char;
        }
    }

    if (value || row.length > 0) {
        row.push(value);
        rows.push(row);
    }

    return rows;
}

function readFile(input) {
    const file = input.files[0];
    const reader = new FileReader();
    const name = file.name;
    reader.readAsText(file);
    reader.onload = function() {
	const data = reader.result;
	if(data.match(/^\s*\{/)) {
	    const json = JSON.parse(data);
	    import_json(json, name);
	} else {
	    /* Assume CSV convert it to JSON schema version 2.0.0*/
	    const rows = simpleCSV(data);
	    let json = simpleCopy(decision_trees[0].data);
	    json.decision_points = {};
	    json.mapping = [];
	    json.name = name.substr(0,name.lastIndexOf('.'));
	    json.key = uniq_key({name: json.name}, decision_trees.map(x => x.data));
	    json.namespace = default_namespace + "/csvupload";
	    json.definition = json.name + " uploaded as CSV";
	    let headers = rows.shift();
	    let hasrowIndex = false;
	    if(headers[0] == "row") {
		headers.shift();
		hasrowIndex = true;
	    }
	    let keymap = [];
	    headers.forEach(function(header,i ) {
		let head = header;
		if(header.indexOf(":") > -1)
		    head = header.split(":")[1];
		let dpkey = uniq_key({name:head},Object.values(json.decision_points));
		keymap[i] = json.namespace.substr(0,3) + ":" + dpkey + ":1.0.0";
		json.decision_points[keymap[i]] = {name: head, namespace: json.namespace,
						   definition: head,
						   key: dpkey};
	    });
	    json.outcome = keymap.at(-1);
	    let valueSet = result = Array.from({ length: headers.length }, () => []);
	    let mapping = [];
	    rows.forEach(function(row) {
		let nmap = {}
		row.forEach(function(value,i) {
		    if(!valueSet[i].some(function(values) { return values.name == value})) {
			let mkey = uniq_key({name:value}, valueSet[i]);
			valueSet[i].push({name: value, definition: value,
					  key: mkey});
			nmap[keymap[i]] = mkey; 
		    } else {
			let lfind = valueSet[i].find(function(valset) {
			    return valset.name == value;
			});
			nmap[keymap[i]] = lfind.key;
		    }
		    
		});
		mapping.push(nmap);
	    });
	    json.mapping = mapping;
	    console.log(json,valueSet);
	    for(let i=0; i<Object.keys(json.decision_points).length; i++)
		json.decision_points[keymap[i]].values = valueSet[i];
	    import_json(json, json.name);
	}
    };
    reader.onerror = function() {
	console.log(reader.error);
	topalert("Reading data in file as text failed","danger")
    };
}
function computeFI(features,labels) {
    /* compute feature Importance */
    /* Decision Tree Classifier */
    function DecisionTreeClassifier() {
	this.rules = null;

	this.train = function (features, labels) {
	    const rules = {};
	    features.forEach((feature, i) => {
		const key = feature.join(',');
		if (!rules[key]) rules[key] = {};
		rules[key][labels[i]] = (rules[key][labels[i]] || 0) + 1;
	    });

	    this.rules = {};
	    for (const key in rules) {
		const outcomes = rules[key];
		this.rules[key] = Object.keys(outcomes).reduce((a, b) =>
		    outcomes[a] > outcomes[b] ? a : b
		);
	    }
	};

	this.predict = function (feature) {
	    const key = feature.join(',');
	    return this.rules[key] || 'unknown'; 
	};
    }

    /* Calculate Accuracy */
    function calculateAccuracy(model, features, labels) {
	const predictions = features.map(row => model.predict(row));
	const correct = predictions.filter((pred, i) => pred === labels[i]).length;
	return correct / labels.length;
    }
    const classifier = new DecisionTreeClassifier();
    classifier.train(features, labels);
    const baselineAccuracy = calculateAccuracy(classifier, features, labels);
    featureNames = Object.keys(decision_table[0]);
    featureNames.pop()
    const fI = featureNames.map((feature, index) => {
	const reducedFeatures = features.map(row => row.filter((_, colIndex) => colIndex !== index));

	const reducedClassifier = new DecisionTreeClassifier();
	reducedClassifier.train(reducedFeatures, labels);

	const reducedAccuracy = calculateAccuracy(reducedClassifier, reducedFeatures, labels);

	return {
	    feature,
	    importance: baselineAccuracy - reducedAccuracy
	};
    });
    return fI;
}
function fun_execute(w) {
    if(w.selectedIndex) {
	try {
	    let find_fun = new Function("return " + w.value + "()");
	    find_fun();
	} catch(err) {
	    console.log("Error when trying to find dynamic function ", err);
	}
	w.selectedIndex = 0;		
    }
}
    return {
	ssvc_launch: ssvc_launch,
	decision_trees: decision_trees,
	form: form,
	loadSSVC: loadSSVC,
	readFile: readFile,
	customize: customize,
	fun_execute: fun_execute,
	toggleAll: toggleAll,
	updateTree: updateTree,
	popupEnd: popupEnd,
	textAreaAutoSize: textAreaAutoSize,
	dpValueClone: dpValueClone,
	__version__: __version__
    }
})();



