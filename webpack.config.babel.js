import path from 'path'
import webpack from 'webpack'
import jsonImporter from 'node-sass-json-importer'


export default {
   entry:  './web_client/app.js',
   output:  {
       path: path.resolve(__dirname, 'static'),
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
//   plugins: [
//       new webpack.LoaderOptionsPlugin({
//           options: {
//               sassLoader: {
//                   importer: jsonImporter,
//               },
//               context: __dirname,
//           },
//       }),
//   ]
}