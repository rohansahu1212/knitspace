const express = require('express')
const app = express();


 app.get('/billu', (req,res)=>{
  res.send("billu here or kya kar rahe")
 } );

 app.listen(3000,()=>{
     console.log("running bht hi sahi")
 });