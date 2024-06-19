#!/usr/bin/node
exports.callMeMoby = function callMeMoby (n, theFunction) {
  for (let i = 0; i < n; i++) {
    theFunction ();
  }
};
