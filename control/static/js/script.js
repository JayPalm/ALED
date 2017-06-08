
//var xx = process.argv[2];
//var yy = process.argv[3];
function grid (xx,yy) {

	for (var i = 0; i <= xx-1; i++) {
		var row = $("<div>");
		row.appendTo($("#array"));
		for (var j = 0; j <= yy-1; j++) {
			var item = $("<input class = jscolor {onFineChange:''}>")
			item.appendTo(row)	
		}
	}
	jscolor.installByClassName("jscolor");
	
	$("input.jscolor").each(function(){
		this.jscolor.onFineChange=function(){
			console.log(this.toHEXString())
		}
	});

}
function randColor (dType="string") {
	$("input.jscolor").each(function(){
		var hEX = ("000000" + Math.random().toString(16).slice(2, 8).toUpperCase()).slice(-6);
		$(this)[0].jscolor.fromString(hEX);
	});
	return(report(dType))
}

function report (dType="string") {
	var arr = [];
	$("input.jscolor").each(function(){
		if (dType.toLowerCase()=="string") {arr.push($(this)[0].jscolor.toString());}
		else if (dType.toLowerCase()=="hex") {arr.push($(this)[0].jscolor.toHEXString());}
		else if (dType.toLowerCase()=="rgb") {arr.push($(this)[0].jscolor.toRGBString());}
	}); 
	return(arr);
}




$(function(){
	jscolor.installByClassName("jscolor");

	xx=$("#xPixels").val();
	yy=$("#yPixels").val();
	grid(xx,yy);

	$("pinput.jscolor").each(function(){
		$(this).change(function(){
			console.log("changed")})
	});

	//$("input").first()[0].onchange=(randColor());

});


jQuery('<input>', {
    id: 'j',
    class:'jscolor',
    value:'#6EFF9E'
}).appendTo('row');

$('.jscolor').each(function(){
    document.getElementById($(this).attr('id')).jscolor.fromString($(this).val());
}); 
