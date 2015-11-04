
 $(document).ready(function () {
    var counter= {
        male: 0,
        female:0,
        age1:0,
        age2:0,
        age3:0
    };
      var agechart = c3.generate({
        bindto: '#ageChart',
        data: {
        // iris data from R
        columns: [
            ['< 10', 30],
            ['10-16', 44],
            ['17-23', 183],
            ['24-30', 120],
            ['31-37', 208],
            ['38-50', 74],
            ['51-59', 86],
            ['>60', 100],
        ],
        type : 'pie',
    }
});
    var genderchart = c3.generate({
    bindto: '#genderChart',
    data: {
        // iris data from R
        columns: [
            ['men', 30],
            ['women', 120],
        ],
        type : 'pie',
    }
});

});