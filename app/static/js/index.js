var headers = {
    0: "alumni_employment",
    1: "broad_impact",
    2: "citations",
    3: "country",
    4: "id",
    5: "influence",
    6: "institution",
    7: "national_rank",
    8: "patents",
    9: "publications",
    10: "quality_of_education",
    11: "quality_of_faculty",
    12: "score",
    13: "world_rank",
    14: "year"
}

var UniveristyRankingTable = function () {
    this.tableId = '#univeristy-ranking-table';

    this.table = $(this.tableId).DataTable({
        "dom": '<"rankings-control">Bfrtip',
        "ajax": {
            "url": "/api/university-ranking",
            "dataSrc": "data",
            "cache": true,
        },
        'pageLength': '25',
        'order': [],
        'aoColumns': [
            { 'mData': 'world_rank'},
            { 'mData': 'national_rank'},
            { 'mData': 'id'},
            { 'mData': 'institution'},
            { 'mData': 'country'},
            { 'mData': 'alumni_employment'},
            { 'mData': 'broad_impact'},
            { 'mData': 'citations'},
            { 'mData': 'influence'},
            { 'mData': 'patents'},
            { 'mData': 'publications'},
            { 'mData': 'quality_of_education'},
            { 'mData': 'quality_of_faculty'},
            { 'mData': 'score'},
            { 'mData': 'year'}
        ],
        'columnDefs': [
            {
                'targets': [5, 6, 7, 8, 9, 10, 11, 12],
                'visible': false,
            }
        ],
        "deferRender": true,
        "scrollY": 1000,
        "scrollX": true,
        "scrollCollapse": true,
        "scroller": true,
        initComplete: function () {
            var select = $("<select></select>").attr("id", 'year-selector').addClass("year-selector form-control");

            var year = 'year';
            select.append( $('<option value="">'+year+'</option>') );

            $('.university-ranking-control').append(select);

            universityRankingTable.table
                .column( 14 )
                .cache( 'search' )
                .sort()
                .unique()
                .each( function ( d ) {
                    select.append( $('<option value="'+d+'">'+d+'</option>') );
                } );

            select.on( 'change', function () {
               universityRankingTable.table
                    .column( 14 )
                    .search( $(this).val() )
                    .draw();
            });

            var lastYear = $('#year-selector option').last().val();
            $('#year-selector').val(lastYear);
            universityRankingTable.table
                    .column( 14 )
                    .search(lastYear)
                    .draw();
        }
    });
};

var mountGraphsAnalyses = function () {
    var top_univeristies = [];

    $.ajax({
            url: '/api/university-ranking',
            success: function (response) {
                for (var i = 0; i < 25; i++) {
                    top_univeristies.push({
                        'world_rank': response.data[i].world_rank,
                        'national_rank': response.data[i].national_rank,
                        'id': response.data[i].id,
                        'institution':response.data[i].institution,
                        'country': !response.data[i].country,
                        'score':response.data[i].score,
                    });
                };

                var visualization = d3plus.viz()
                    .container("#bar-top-universities")
                    .data(top_univeristies)
                    .type("bar")
                    .id("institution")
                    .x({"value": "institution", "label": false, "grid": false})
                    .y({"value": "score", "label": false, "range": [0, 100]})
                    .labels({"padding": 30})
                    .order({"sort": "asc", "value":"score"})
                    .color({"scale": ["#1DB954"]})
                    .background("#fff")
                    .axes({"background": {"color": "#fff"}})
                    .title("Top 25 Universities")
                    .title({"font":{ "size": "25px", "family": "Raleway" }})
                    .draw()
            }
    });
}

window.universityRankingTable = new UniveristyRankingTable();

mountGraphsAnalyses();

$(document).ready(function() {
    $.localScroll({
        offset: 0,
        duration: 1200
    });
});


