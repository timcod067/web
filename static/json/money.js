var data;
$(document).ready(
    function () {

        $('#inputid').click(
            function () {
                console.log($('#Station1').val());
                let sation1 = $('#Station1').val();
                let sation2 = $('#Station2').val();
                console.log($('#Station2').val());
                var GoUrl = `https://ptx.transportdata.tw/MOTC/v2/Rail/TRA/ODFare/${sation1}/to/${sation2}?%24top=30&%24format=JSON`;
                $.ajax({
                    url: GoUrl,
                    // url: "../json/money.json",
                    method: 'GET',
                    dataType: 'json',
                    data: '',
                    async: true,

                    success: function (items) {
                        console.log(items);
                        data = items;
                        $("#trinfo").empty();
                        for (var i = 0; i < items[0].Fares.length; i++) {
                            var train = $("<tr>");
                            var num = $("<td>");
                            var TicketType = $("<td>");
                            var Price = $("<td>");
                            num.html(i);
                            TicketType.html(items[0].Fares[i].TicketType);
                            Price.html(items[0].Fares[i].Price+"元");
                            train.append(num,TicketType, Price);
                            $("#trinfo").append(train);
                        }
                    }
                });
            }
        )
    }
);
