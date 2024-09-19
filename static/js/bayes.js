function Bayes() {
    var px = parseFloat(document.getElementById("Px").value);
    var py = parseFloat(document.getElementById("Py").value);
    var pxy = parseFloat(document.getElementById("Pxy").value);
    var pyx = parseFloat(document.getElementById("Pyx").value);
    
    console.log("px", px, "py", py, "pxy", pxy, "pyx", pyx);

    if (!checkvalid(px, py, pxy, pyx)) {
        document.getElementById("result").innerHTML = "Invalid calculation. Check your input values. <br>Ensure atleast 3 are entered";
        return;
    }
    
    fetch('/calculate_bayes',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({px,py,pxy,pyx})
    })
    .then(response =>response.json())
    .then(data => {
        document.getElementById('result').textContent = data.prob + data.bayes_result
    })

    
}
