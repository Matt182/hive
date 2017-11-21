import path from 'path'
import webpack from 'webpack'

export default {
   entry:  './static_source/app.js',
   output:  {
       path: path.resolve(__dirname, 'public/js'),
       filename: 'app.js'
   },
   module: {
       rules: [
           {
               test: /\.js$/,
               use: 'babel-loader'
           },
           {
               test: /\.s[a|c]ss$/,
               use: [
                   'style-loader!css-loader!sass-loader'
               ]
           }
       ]
   },
}