$(document).ready(function() {
    $("#sample_1").dataTable(
        {
            searching : false,
            destroy : true,
            "ajax": {
                "url": "video/query/",
                "type": "get",
                "dataSrc":"",
            },
            columns: [
                { },
                { data: 'filename' },
                { data: 'is_processed' },
                { data: 'create time'},
                { }
            ],
            'columnDefs': [{
                'targets': 0,
                'searchable': true,
                'orderable': true,
                'className': 'select-checkbox',
                'render': function (data, type, full, meta){
                return  '<label class="mt-checkbox mt-checkbox-single mt-checkbox-outline"><input type="checkbox" class="checkboxes" value="1"/><span></span></label>'
                }
            }],
         }
    );
});