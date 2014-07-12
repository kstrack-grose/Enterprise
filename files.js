//files.js

var fs = require('fs')

var path = '/home/kiri/Code/NODE/public/static/media'

for (var i = 0; i < fs.readdirSync(path).length; i++) {
	<img src=path+'/'+fs.readdirSync[i] width="400" height="300" align="left" hspace="20">
};