class TestCalcDist:
    "Test that the calcDist method works"

    // Aberdeen st, NB
    lat1 = -31.947571;
    lon1 = 115.861860;

    // Antonas rd, NB
    lat2 = -31.944165;
    lon2 = 115.855300;

    // Davies st, NB
    lat3 = -31.944358;
    lon3 = 115.855509;

    // Errichetti pl, NB
    lat4 = -31.946280;
    lon4 = 115.859189;

    def test1():
        """ Test distance between Aberdeen st and Antonas rd"""
        dist1 = CalcDist.calcDistKm(lat1, lon1, lat2, lon2);
        print('The distance between Aberdeen st and Antonas rd: ', dist1);

    def test2():
        """ Test distance between Antonas rd and Davies st"""
        dist2 = CalcDist.calcDistKm(lat2, lon2, lat3, lon3);
        print('The distance between Antonas rd and Davies st: ', dist2);

    def test3():
        """ Test distance between Davies st and Errichetti pl"""
        dist3 = CalcDist.calcDistKm(lat3, lon3, lat4, lon4);
        print('The distance between Davies st and Errichetti pl: ', dist3);
