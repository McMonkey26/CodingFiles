const fs = require("fs")
const priceData = require("./priceData.json")
function recipeCost(itemid){
  return Object.entries(recipes[itemid] ?? {}).map(([item,count]) => costs[item]*Number(count)).reduce((a, b) => a + b, 0) || 0
}

function getPriceMarginPercent(itemid){
  return costs[itemid] / recipeCost(itemid) * 100
}
function getPriceMarginFlat(itemid){
  return costs[itemid] - recipeCost(itemid)
}


let costs = {'ABSOLUTE_ENDER_PEARL':12500, 'VORPAL_KATANA':10000000, 'ENCHANTED_ENDER_PEARL': 150}
let recipes = {'ABSOLUTE_ENDER_PEARL': {"ENCHANTED_ENDER_PEARL":16,"ENCHANTED_ENDER_PEARL":16,"ENCHANTED_ENDER_PEARL":16,"ENCHANTED_ENDER_PEARL":16,"ENCHANTED_ENDER_PEARL":16}, 'VORPAL_KATANA':{"ABSOLUTE_ENDER_PEARL":24}}
let itemDatas = {'recipeCost':{},'priceMarginPercent':{},'priceMarginFlat':{}}
for (let x in Object.keys(costs)) {
  itemDatas.recipeCost[x] = recipeCost(x)
  itemDatas.priceMarginPercent[x] = getPriceMarginPercent(x)
  itemDatas.priceMarginFlat[x] = getPriceMarginFlat(x)
}

const maxMarginPercent = Object.entries(itemDatas.priceMarginPercent).reduce((a, b) => a[1] > b[1] ? a : b)[0]
const maxMarginFlat = Object.entries(itemDatas.priceMarginFlat).reduce((a, b) => a[1] > b[1] ? a : b)[0]
//for (let x in Object.keys(costs)) {
x = "ABSOLUTE_ENDER_PEARL"
// priceData.itemid = x
priceData.recipeCost = recipeCost(x)
priceData.priceMarginPercent = getPriceMarginPercent(x)
priceData.priceMarginFlat = getPriceMarginFlat(x)
fs.writeFile("./priceData.json", JSON.stringify(priceData, null, 2), function writeJSON(err) {
  if (err) return console.log(err);
  console.log(JSON.stringify(priceData, null, 2));
  console.log('writing to ' + "./priceData.json");
});
