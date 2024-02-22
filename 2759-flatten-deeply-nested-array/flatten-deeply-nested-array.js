/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let flattened = [];

        function flattenHelper(arr, depth) {
            arr.forEach(element => {
                if (Array.isArray(element) && depth < n) {
                    flattenHelper(element, depth + 1);
                } else {
                    flattened.push(element);
                }
            });
        }

    flattenHelper(arr, 0);
    return flattened;
};