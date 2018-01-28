import path from 'path'
import webpack from 'webpack'
import ExtractTextPlugin from 'extract-text-webpack-plugin'

const extractSass = new ExtractTextPlugin({
  filename: "styles.css",
});

export default {
   entry:  {
       friend: './static_source/friend.js',
       post_and_comm: './static_source/post_and_comment.js'
   },
   output:  {
       path: path.resolve(__dirname, 'public/js'),
       filename: '[name].entry.js'
   },
   module: {
       rules: [
           {
               test: /\.js$/,
               use: {
                   loader: 'babel-loader',
                   options: {
                       ignore: './node_modules/',
                       presets: [
                           ['es2015', { modules: false }]
                       ]
                   }
               }
           },
           {
               test: /\.s[a|c]ss$/,
               use: extractSass.extract({
                   fallback: 'style-loader',
                   //resolve-url-loader may be chained before sass-loader if necessary
                   use: [{
                       loader: "css-loader" // translates CSS into CommonJS
                   }, {
                       loader: "sass-loader" // compiles Sass to CSS
                   }]
               })
           }
       ]
   },
   plugins: [
       new webpack.ProvidePlugin({
           $: "jquery", // Used for Bootstrap JavaScript components
           jQuery: "jquery", // Used for Bootstrap JavaScript components
           //Popper: ['popper.js', 'default'] // Used for Bootstrap dropdown, popup and tooltip JavaScript components
       }),
       extractSass
   ]
}