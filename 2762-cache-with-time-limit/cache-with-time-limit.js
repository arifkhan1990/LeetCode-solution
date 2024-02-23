var TimeLimitedCache = function() {
    this.cache = {};
    this.expiryTimes = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    var currentTime = Date.now();
    var expiryTime = currentTime + duration;

    if (this.cache.hasOwnProperty(key) && this.expiryTimes[key] > currentTime) {
        this.cache[key] = value;
        this.expiryTimes[key] = expiryTime;
        return true;
    } else {
        this.cache[key] = value;
        this.expiryTimes[key] = expiryTime;
        return false;
    }
};


/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    var currentTime = Date.now();
    if(this.cache.hasOwnProperty(key) && this.expiryTimes[key] > currentTime) {
        return this.cache[key];
    }else {
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    var currentTime = Date.now();
    var count = 0;
    for (var key in this.cache) {
        if (this.cache.hasOwnProperty(key) && this.expiryTimes[key] > currentTime) {
            count++;
        }
    }
    return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */