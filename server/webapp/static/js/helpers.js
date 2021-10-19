$(function () {
	$('#loading').hide();
	$('#additionalField1').hide();
	$('#additionalField2').hide();
	$('[data-toggle="tooltip"]').tooltip();

	$('#nodeIp').change(function () {
		var selectedValue = $(this).val();
		console.log(selectedValue);
		if (selectedValue !== null && selectedValue !== '') {
			$.ajax({
				type: 'GET',
				url: '/v1/interfaces',
				data: "node=" + selectedValue,
				success: function (response) {
					$('#interface').empty();
					for (var key in response) {
						if (response.hasOwnProperty(key)) {
							var value = response[key];
							$('#interface').append('<option value="' + value + '">' + value + '</option>');
						}
					}
					$('#additionalField1').show();
					$('#additionalField2').show();
				}
			});
		}
	})


	/*$('#btnSubmit').click(function (e) {
		$('#content').hide();
		$('#alerts').hide();
		$('#loading').show();
		var progressBar = $('#progress_bar'),
			width = 0;
		progressBar.width(width);

		var interval = setInterval(function () {
			width += 0.5;
			progressBar.css('width', width + '%');

			if (width >= 100) {
				//clearInterval(interval);
				width -= 10;
			}
		}, 1000);
	});*/
});

window.setTimeout(function () {
	$('.alert').fadeOut('fast')
}, 10000);
