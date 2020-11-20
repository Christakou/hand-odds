```
var a = document.querySelectorAll("[class*='hearts'],[class*='diamonds'],[class*='spades'],[class*='clubs']")
var b = document.querySelectorAll("[class*='details']")
console.log(b)
for(let i=0; i<a.length; i++){
  string+=a[i].outerHTML+','
}
string+= b.length
console.log(string)
```