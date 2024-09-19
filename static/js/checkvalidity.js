function checkvalid(px,py,pxy,pyx){
    if (px===0){
        if (py===0 || pxy ===0 || pyx ===0){
            return false
        }
    }
    else if(py === 0){
        if(pxy === 0 || pyx == 0){
            return false
        }
    }
    else if(pxy ===0 && pyx ===0){
        return false
    }
    return true
}