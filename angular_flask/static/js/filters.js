'use strict';

/* Filters */

angular.module('angularFlaskFilters', []).filter('unique', function() {
return function ( collection, keyname) {
    var output = [],
        keys = [],
        found = [];

    if (!keyname) {

        angular.forEach(collection, function (row) {
            var is_found = false;
            angular.forEach(found, function (foundRow) {

                if (foundRow == row) {
                    is_found = true;                            
                }
            });

            if (is_found) { return; }
            found.push(row);
            output.push(row);

        });
    }
    else {

        angular.forEach(collection, function (row) {
            var item = row[keyname];
            if (item === null || item === undefined) return;
            if (keys.indexOf(item) === -1) {
                keys.push(item);
                output.push(row);
            }
        });
    }

    return output;
}
});
