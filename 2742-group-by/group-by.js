/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    var mp = {};
    for (var i = 0; i < this.length; i++) {
        var key = fn(this[i]);
        if (!(key in mp)){
            mp[key] = [];
        }
        mp[key].push(this[i]);
    }
    return mp;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */