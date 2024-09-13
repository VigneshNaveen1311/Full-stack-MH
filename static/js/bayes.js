function Bayes() {
    var px = parseFloat(document.getElementById("Px").value);
    var py = parseFloat(document.getElementById("Py").value);
    var pxy = parseFloat(document.getElementById("Pxy").value);
    var pyx = parseFloat(document.getElementById("Pyx").value);
    var result;
    
    console.log("px", px, "py", py, "pxy", pxy, "pyx", pyx);

    if (!checkvalid(px, py, pxy, pyx)) {
        document.getElementById("result").innerHTML = "Invalid calculation. Check your input values. <br>Ensure atleast 3 are entered";
        return;
    }
    var prob;
    if (px === 0) {
        result = pxy * py / pyx;
        prob = "Prior probability P(X): "
    } else if (py === 0 ) {
        result = pyx * px / pxy;
        prob = "Marginal Likelihood P(Y) : "
    } else if (pxy === 0 ) {
        result = pyx * px / py;
        prob = "Posterior probability P(X|Y) : "
    } else  {
        result = pxy * py / px;
        prob = "Likelihood P(Y|X) : "
    }

    if (result > 1) {
        document.getElementById("result").innerHTML = "Invalid values";
    } else {
        document.getElementById("result").innerHTML = prob + result;
    }
    document.getElementById("currfile").innerHTML = "JS";
}
