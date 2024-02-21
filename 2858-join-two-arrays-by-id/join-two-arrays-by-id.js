/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const mergedMap = arr1.concat(arr2).reduce((map, obj) => {
        const id = obj.id;
        if(!map.has(id)) {
            map.set(id, {});
        }
        Object.assign(map.get(id), obj);
        return map;
    }, new Map());

    return Array.from(mergedMap.values()).sort((a,b) => a.id - b.id);
};