var trs = document.querySelectorAll('tr.hover');
var tr_op_all = document.querySelectorAll('tr.hover .opacity');

trs.forEach(function(tr) {
    tr.addEventListener('click', function() {
        trs.forEach(function(trss) {
            trss.style.background = "white";            
        })
        tr.style.background = "aqua";
        tr_op_all.forEach(function(trop) {
            trop.style.opacity = "0";
        })
        var tr_op = tr.querySelectorAll('.opacity');
        tr_op.forEach(function(tr_ops) {
            tr_ops.style.opacity = "1";
        })
    })
})

