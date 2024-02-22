/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.map(compactObject).filter(Boolean);
    }else if(typeof obj === "object" && obj !== null) {
        return Object.fromEntries(
            Object.entries(obj)
                .map(([key, value]) => [key, compactObject(value)])
                .filter(([_, value]) => Boolean(value))
        );
    }else{
        return obj;
    }
};