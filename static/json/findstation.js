var dd = "";

$(document).ready(
    function () {

        // alert("hi")
        $.ajax({
            // url: originUrl,
            url: "/static/json/rstationtime.json",
            method: 'GET',
            dataType: 'json',
            data: '',
            async: true,
            success: function (items) {
                dd = items;
                
                $("#inputid").click(function () {
                    $("#ffstation").val("");
                    $("#s").empty();
                    $("#ffstation").empty();
                    var onetime = "";
                    var twotime = "";
                    var threetime = "";
                    // console.log(items[1].StaionTimetables.StationID)
                    var id = $("#startStation").val()
                    // alert(id)
                    // var long = dd[0].StationTimetables.length
                    // var twolong = dd[0].StationTimetables[0].TimeTables.length
                    $("#searchcity").empty();
                    for (var i = 0; i < items.length; i++) {
                        if (id == dd[i].DailyTrainInfo.StartingStationID) {
                            var startstation = dd[i].DailyTrainInfo.StartingStationName.Zh_tw;
                            console.log(startstation)
                            var endstation = dd[i].DailyTrainInfo.EndingStationName.Zh_tw;
                            var trainto = $("<tr>");
                            var aa = dd[i].StopTimes.length;
                            var bb = dd[i].DailyTrainInfo.StartingStationID
                            console.log(aa)
                            trainto.attr("id", bb)
                            trainto.attr("class", "traincs");
                            trainto.append("起點站：", startstation);
                            trainto.append(" -> 終點站：", endstation);
                            // $("#searchcity").append(trainto);
                            for (var j = 0; j < aa; j++) {
                                var train = $("<tr>");
                                var trainonetime = $("<td>");
                                var traintwotime = $("<td>");
                                var trainthreetime = $("<td>");
                                onetime = dd[i].StopTimes[j].StationName.Zh_tw;
                                twotime = dd[i].StopTimes[j].ArrivalTime;
                                threetime = dd[i].StopTimes[j].DepartureTime;
                                trainonetime.html( onetime);
                                traintwotime.html( twotime);
                                trainthreetime.html( threetime);
                                train.append(trainonetime);
                                train.append(traintwotime);
                                train.append(trainthreetime);
                                $("#s").append(train);
                            }
                            
                        } 
                    }

                })
            }
            
        });
        
    });

