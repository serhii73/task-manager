$(document).ready(function () {
    $("#id_name_task, #id_category_task").change(function () {
        var name_task = $("#id_name_task").val();
        var id_category = $("#id_category_task").val();
        $.ajax({
            type: 'GET',
            async: true,
            dataType: 'json',
            url: '{% url "validate_data" %}',
            data: {
                'name_task': name_task,
                'id_category': id_category,
            },
            success: function (data) {
                if (data.is_taken) {
                    alert("A task with this name already exists.");
                }

            },
        });
    });
});