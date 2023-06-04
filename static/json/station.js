const cityname = ["基隆市", "新北市", "臺北市", "桃園市", "新竹縣", "新竹市", "苗栗縣", "臺中市", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市", "臺南市", "高雄市", "屏東縣", "臺東縣", "花蓮縣", "宜蘭縣"];
const cityid = ["KEE", "NWT", "TPE", "TAO", "HSQ", "HSZ", "MIA", "TXG", "CHA", "NAN", "YUN", "CYQ", "CYI", "TNN", "KHH", "PIF", "TTT", "HUA", "ILA"];
var da = '';
var daa = '';
var str = '';
var clickid = '';
var check = 0;
var citybutton = "tpe";
$(document).ready(
    function () {

        $.ajax({
            // url: originUrl,
            url: "../json/station location.json",
            method: 'GET',
            dataType: 'json',
            data: '',
            async: true,

            success: function (items) {
                for (var i = 0; i < cityname.length; i++) {
                    var station_location_id = $("<button>");
                    station_location_id.attr("id", cityid[i]);
                    station_location_id.attr("class", citybutton + " btn btn-outline-primary");
                    station_location_id.append(cityname[i]);
                    $("#station2").append(station_location_id);
                }

                $(".tpe").click(function () {
                    var id = $(this).attr("id");
                    for (var j = 0; j < items.length; j++) {


                        if (id === items[j].LocationCityCode) {
                            var test = items[j].LocationCityCode;
                            console.log(test);
                            $("." + id).css("display", "block");

                        } else {
                            var test2 = items[j].LocationCityCode;
                            $("." + test2).css("display", "none");
                        }
                    }
                    $("." + id).click(function () {
                        var stationid = $(this).attr("id");
                        console.log(stationid);
                        $("#startStation").val(stationid);
                    });
                });


            }
        });

        $.ajax({
            // url: originUrl,
            url: "../json/station location.json",
            method: 'GET',
            dataType: 'json',
            data: '',
            async: true,

            success: function (items) {
                da = items;
                for (var i = 0; i < items.length; i++) {
                    var trainstation_location = $("<button>");
                    trainstation_location.attr("id", items[i].StationID);
                    trainstation_location.attr("style", "display:none");
                    trainstation_location.attr("data-type", "taiwan");
                    trainstation_location.addClass(`${items[i].LocationCityCode} btn btn-outline-secondary tranbtn`);
                    trainstation_location.append(items[i].StationName.Zh_tw);
                    $("#station2son").append(trainstation_location);
                }
            }
        });

    }
);











