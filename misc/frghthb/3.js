const fs = require('fs');
const path = 'polygons.txt';

function isTriangle(polygon){
	return polygon.length==3 && (polygon[0]+polygon[1]>polygon[2])
			&& (polygon[0]+polygon[2]>polygon[1])
			&& (polygon[2]+polygon[1]>polygon[0]);
};

function isRectangle(polygon){
	return polygon.length==4;
}

function isSquare(polygon){
	if (!isRectangle(polygon)){
		return false;
	}
	return polygon.every(e=>e==polygon[0]);
}

fs.readFile(path, function (err, file) {
	if (err){
		throw err;
	}
	file = file.toString();
	var polygons = file.split('\n').map(line => line.split(',').map(side => parseInt(side)).filter(side => side>0)).filter(p=>p.length>0);

	// NOTE: I can optimize by removing categorized types after each step 
	// so that next one has less iterm to proceed, but not enough time so maybe next time.
	var triangles = polygons.filter(isTriangle);
	var rectangles = polygons.filter(p => isRectangle(p) && !isSquare(p));
	var squares = polygons.filter(isSquare);
	var everythingElse = polygons.filter(p => !isTriangle(p) && !isRectangle(p));

	console.log('triangles: ',triangles);
	console.log('rectangles: ',rectangles);
	console.log('squares: ',squares);
	console.log('everythingElse: ',everythingElse);
});
