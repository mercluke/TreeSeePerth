class CalcDist
{
  // haha I don't know how to use JavaScript.. or Python, but I guess that is
  // why you're taking FOP next sem? :D

  function calcDistKm(lat1, lon1, lat2, lon2)
  {
    var rad = 6371; //Radius of the earth in km
    var dLat = degToRad(lat2 - lat1);
    var dLon = degToRad(lon2 - lon1);
    var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(degToRad(lat1)) * Math.cos(degToRad(lat2)) *
            Math.sin(dLon/2) * Math.sin(dLon/2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return rad * c;
  }

  function degToRad(deg)
  {
    return deg * (Math.PI/180);
  }

}
