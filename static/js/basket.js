window.onload = function() {
	$('.basket_list').on('click', 'input[type="number"]', function () {
		var target = event.target;

		$.ajax({
			url: '/baskets/edit/' + target.name + '/' + target.value + '/',
			success: function (data) {
				$('.basket_list').html(data.result),
				$('.basket_load').html(data.result_load)
			},
		});
	});

	$('.basket_add').on('click', 'button', function () {
		var target = event.target;

		$.ajax({
			url: '/baskets/add/' + target.name,
			success: function (data) {
				$('.basket_load').html(data.result)
			},
		});
	});
}