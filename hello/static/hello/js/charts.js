
  $(document).ready(function () {
c3.generate({
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
        type : 'bar',
    },
    bar: {
        width: {
            ratio: 0.5 // this makes bar width 50% of length between ticks
        }
        // or
        //width: 100 // this makes bar width 100px
    }
});

      var whenchart = c3.generate({
    bindto: '#whenChart',
    data: {
        // iris data from R
        columns: [
            ['last week', 30],
            ['2 weeks ago', 172],
            ['3 weeks ago', 99],
            ['a month ago', 150],


        ],
        type : 'donut',
    },
    donut: {
        title: "Traffic distribution"
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
    
