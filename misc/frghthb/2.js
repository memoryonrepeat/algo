const requests = [
{requestId: 'poiax',  startedAt: 1489744808, ttl: 8},
{requestId: 'kdfhd',  startedAt: 1489744803, ttl: 3},
{requestId: 'uqwyet', startedAt: 1489744806, ttl: 12}, 
{requestId: 'qewaz',  startedAt: 1489744810, ttl: 1}
]

const cumulativeTtl = 15

function getCumulativeTTL(requests) {
	var latest = 0;
	var earliest = requests[0].startedAt;
	requests.forEach(function(request){
		latest = (request.startedAt+request.ttl > latest) ? request.startedAt+request.ttl : latest;
		earliest = (request.startedAt < earliest) ? request.startedAt : earliest;
	});
	return latest-earliest;
};

console.log(getCumulativeTTL(requests));