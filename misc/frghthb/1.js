const startingArray = [2, 4, 6, 8, 9, 15]
const resultingArray = ['4', '16', '64']

function transform(arr) {
	return arr.filter(isOnlyDivisibleBy2).map(num => (num*num).toString());
}

function isOnlyDivisibleBy2(num){
	if (!Number.isInteger(num)){
		return false;
	}
	if (num==2){
		return true;
	}
	return isOnlyDivisibleBy2(num/2);
}

console.log(transform(startingArray));