// https://leetcode.com/problems/design-hit-counter/submissions/

/**
 * Initialize your data structure here.
 */
var HitCounter = function() {
    this.table = {}
};

/**
 * Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). 
 * @param {number} timestamp
 * @return {void}
 */
HitCounter.prototype.hit = function(timestamp) {
    if (timestamp in this.table){
        this.table[timestamp] += 1
        return
    }
    
    this.table[timestamp] = 1
};

/**
 * Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). 
 * @param {number} timestamp
 * @return {number}
 */
HitCounter.prototype.getHits = function(timestamp) {
    const lowerBound = timestamp - 300
    let result = 0
    for (let i=lowerBound+1; i<timestamp+1; i++){
        if (i in this.table){
            result += this.table[i]
        }
    }
    
    return result
};

/** 
 * Your HitCounter object will be instantiated and called as such:
 * var obj = new HitCounter()
 * obj.hit(timestamp)
 * var param_2 = obj.getHits(timestamp)
 */