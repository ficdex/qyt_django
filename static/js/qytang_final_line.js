function formatNumber (n) {
            n = n.toString()
            return n[1] ? n : '0' + n;
        }
        function formatTime (number, format) {
            let time = new Date(number)
            let newArr = []
            let formatArr = ['Y', 'M', 'D', 'h', 'm', 's']
            newArr.push(time.getFullYear())
            newArr.push(formatNumber(time.getMonth() + 1))
            newArr.push(formatNumber(time.getDate()))

            newArr.push(formatNumber(time.getHours()))
            newArr.push(formatNumber(time.getMinutes()))
            newArr.push(formatNumber(time.getSeconds()))

            for (let i in newArr) {
                format = format.replace(formatArr[i], newArr[i])
            }
            return format;
        }

function echart_final_line_if_speed(chartid, labelname, lengends, datas, starttime) {
            let chart = echarts.init(document.getElementById(chartid));//找到HTML中id为chartid的标签

            let option = {
                            title: {
                                text: labelname

                            },
                            tooltip: {
                                formatter: function (params) {
                                    console.log(params)
                                    let res='<div>时间：'+formatTime((params[0].data)[0], 'Y-M-D h:m:s')+'</div>'
                                    res+='<i class="fa fa-circle" style="color:'+params[0].color+'"></i> '+params[0].seriesName.replace(/Av.*/, '')+': '+(params[0].data)[1]+' kbps'+'<br/>'
                                    res+='<i class="fa fa-circle" style="color:'+params[1].color+'"></i> '+params[1].seriesName.replace(/Av.*/, '')+': '+(params[1].data)[1]+' kbps'+'<br/>'
                                    return res;},
                                trigger: 'axis',
                                axisPointer: {
                                    type: 'cross'
                                }
                            },
                            legend: {
                                left: '5%',
                                bottom: '7%',
                                data: lengends
                            },
                            grid: {
                                left: 'left',
                                //right: 1,
                                //bottom: 1,
                                y2: 100,
                                containLabel: true
                            },
                            toolbox: {
                                right: '10%',
                                feature: {
                                    saveAsImage: {} //保存图片功能
                                }
                            },
                            xAxis: {
                                //axisLabel: {
                                  //interval: 30
                                //},只对category类目轴有效
                                splitNumber: 16,
                                type: 'time',
                                boundaryGap: false,
                                //如果type是time就不需要，系列里面的数据是二维数组。data: labels
                            },
                            // 最下面的时间滑动条就是他
                            dataZoom: [{
                                // 开始时间
                                startValue: starttime
                            }, {
                                type: 'inside'
                            }],
                            yAxis: {
                                type: 'value',
                                axisLabel: {
                                    formatter: '{value} kbps' // 格式化,单位为kbps
                                }
                            },
                            series: datas

            };

            chart.setOption(option);
        }

function echart_final_line_cpu_usage(chartid, labelname, lengends, datas, starttime) {
            let chart = echarts.init(document.getElementById(chartid));//找到HTML中id为chartid的标签

            let option = {
                            title: {
                                text: labelname

                            },
                            tooltip: {
                                formatter: function (params) {
                                    console.log(params)
                                    let res='<div>时间：'+formatTime((params[0].data)[0], 'Y-M-D h:m:s')+'</div>'
                                    res+='<i class="fa fa-circle" style="color:'+params[0].color+'"></i> '+params[0].seriesName.replace(/Av.*/, '')+': '+(params[0].data)[1]+' %'+'<br/>'
                                    return res;},
                                trigger: 'axis',
                                axisPointer: {
                                    type: 'cross'
                                }
                            },
                            legend: {
                                left: '5%',
                                bottom: '7%',
                                data: lengends
                            },
                            grid: {
                                left: 'left',
                                //right: 1,
                                //bottom: 1,
                                y2: 100,
                                containLabel: true
                            },
                            toolbox: {
                                right: '10%',
                                feature: {
                                    saveAsImage: {} //保存图片功能
                                }
                            },
                            xAxis: {
                                //axisLabel: {
                                  //interval: 30
                                //},只对category类目轴有效
                                splitNumber: 16,
                                type: 'time',
                                boundaryGap: false,
                                //如果type是time就不需要，系列里面的数据是二维数组。data: labels
                            },
                            // 最下面的时间滑动条就是他
                            dataZoom: [{
                                // 开始时间
                                startValue: starttime
                            }, {
                                type: 'inside'
                            }],
                            yAxis: {
                                type: 'value',
                                axisLabel: {
                                    formatter: '{value} %' // 格式化,单位为%
                                }
                            },
                            series: datas

            };

            chart.setOption(option);
        }

function get_json_render_echart_line_if_speed(url, chartid) {
            $.getJSON(url,function(data) {//请求URL的JSON,得到数据data,下面是对data的处理
                                            echart_final_line_if_speed(chartid, data.labelname, data.lengends, data.datas, data.starttime)
                                          });
            }

function get_json_render_echart_line_cpu_usage(url, chartid) {
            $.getJSON(url,function(data) {//请求URL的JSON,得到数据data,下面是对data的处理
                                            echart_final_line_cpu_usage(chartid, data.labelname, data.lengends, data.datas, data.starttime)
                                          });
            }