"use strict";(self.webpackChunkgraphiql_ui=self.webpackChunkgraphiql_ui||[]).push([[168],{2269:function(e,t,n){n.d(t,{f:function(){return i}});function i(e,t){for(var n=[],i=e;null===i||void 0===i?void 0:i.kind;)n.push(i),i=i.prevState;for(var r=n.length-1;r>=0;r--)t(n[r])}(0,Object.defineProperty)(i,"name",{value:"forEachState",configurable:!0})},3168:function(e,t,n){n.r(t);var i=n(889),r=n(2572),a=n(7382),l=n(2269),o=(n(2223),n(2791),n(4164),Object.defineProperty),u=function(e,t){return o(e,"name",{value:t,configurable:!0})};function f(e,t,n){var i=c(n,p(t.string));if(i){var r=null!==t.type&&/"|\w/.test(t.string[0])?t.start:t.end;return{list:i,from:{line:e.line,ch:r},to:{line:e.line,ch:t.end}}}}function c(e,t){return t?s(s(e.map((function(e){return{proximity:d(p(e.text),t),entry:e}})),(function(e){return e.proximity<=2})),(function(e){return!e.entry.isDeprecated})).sort((function(e,t){return(e.entry.isDeprecated?1:0)-(t.entry.isDeprecated?1:0)||e.proximity-t.proximity||e.entry.text.length-t.entry.text.length})).map((function(e){return e.entry})):s(e,(function(e){return!e.isDeprecated}))}function s(e,t){var n=e.filter(t);return 0===n.length?e:n}function p(e){return e.toLowerCase().replace(/\W/g,"")}function d(e,t){var n=y(t,e);return e.length>t.length&&(n-=e.length-t.length-1,n+=0===e.indexOf(t)?0:.5),n}function y(e,t){var n,i,r=[],a=e.length,l=t.length;for(n=0;n<=a;n++)r[n]=[n];for(i=1;i<=l;i++)r[0][i]=i;for(n=1;n<=a;n++)for(i=1;i<=l;i++){var o=e[n-1]===t[i-1]?0:1;r[n][i]=Math.min(r[n-1][i]+1,r[n][i-1]+1,r[n-1][i-1]+o),n>1&&i>1&&e[n-1]===t[i-2]&&e[n-2]===t[i-1]&&(r[n][i]=Math.min(r[n][i],r[n-2][i-2]+o))}return r[a][l]}function v(e,t,n){var i="Invalid"===t.state.kind?t.state.prevState:t.state,l=i.kind,o=i.step;if("Document"===l&&0===o)return f(e,t,[{text:"{"}]);var u=n.variableToType;if(u){var c=m(u,t.state);if("Document"===l||"Variable"===l&&0===o)return f(e,t,Object.keys(u).map((function(e){return{text:'"'.concat(e,'": '),type:u[e]}})));if("ObjectValue"===l||"ObjectField"===l&&0===o)if(c.fields)return f(e,t,Object.keys(c.fields).map((function(e){return c.fields[e]})).map((function(e){return{text:'"'.concat(e.name,'": '),type:e.type,description:e.description}})));if("StringValue"===l||"NumberValue"===l||"BooleanValue"===l||"NullValue"===l||"ListValue"===l&&1===o||"ObjectField"===l&&2===o||"Variable"===l&&2===o){var s=c.type?(0,r.xC)(c.type):void 0;if(s instanceof r.sR)return f(e,t,[{text:"{"}]);if(s instanceof r.mR)return f(e,t,s.getValues().map((function(e){return{text:'"'.concat(e.name,'"'),type:s,description:e.description}})));if(s===a.EZ)return f(e,t,[{text:"true",type:a.EZ,description:"Not false."},{text:"false",type:a.EZ,description:"Not true."}])}}}function m(e,t){var n={type:null,fields:null};return(0,l.f)(t,(function(t){if("Variable"===t.kind)n.type=e[t.name];else if("ListValue"===t.kind){var i=n.type?(0,r.tf)(n.type):void 0;n.type=i instanceof r.p2?i.ofType:null}else if("ObjectValue"===t.kind){var a=n.type?(0,r.xC)(n.type):void 0;n.fields=a instanceof r.sR?a.getFields():null}else if("ObjectField"===t.kind){var l=t.name&&n.fields?n.fields[t.name]:null;n.type=null===l||void 0===l?void 0:l.type}})),n}u(f,"hintList"),u(c,"filterAndSortList"),u(s,"filterNonEmpty"),u(p,"normalizeText"),u(d,"getProximity"),u(y,"lexicalDistance"),i.C.registerHelper("hint","graphql-variables",(function(e,t){var n=e.getCursor(),r=e.getTokenAt(n),a=v(n,r,t);return(null===a||void 0===a?void 0:a.list)&&a.list.length>0&&(a.from=i.C.Pos(a.from.line,a.from.ch),a.to=i.C.Pos(a.to.line,a.to.ch),i.C.signal(e,"hasCompletion",e,a,r)),a})),u(v,"getVariablesHint"),u(m,"getTypeInfo")}}]);
//# sourceMappingURL=168.97731812.chunk.js.map