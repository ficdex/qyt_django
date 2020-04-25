function echarts_compound(chartid, labelname, legends, labels, datas){
        let myChart = echarts.init(document.getElementById(chartid));
        myChart.setOption({
            title : {
                text:labelname,
                x:'center',
                textStyle:{
                    color: 'red',
                    fontSize: 20
                }
            },
            legend: {
                    bottom: 0,
                    data:legends
                            },
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                name: '时间',
                data: labels,
            },
            yAxis: {
                type: 'value',
                name: '利用率(单位%)',
                axisLabel: {
                            formatter: '{value} %' // 格式化,单位为%
                            },
                min: 0,
                max: 100
            },
            series: datas
        })
    }


function echarts_bar(chartid, labelname, labels, datas, color){
        let myChart = echarts.init(document.getElementById(chartid));

        myChart.setOption({
            title : {
                text:labelname,
                // subtext:"bar",
                x:'center',
                textStyle:{
                    color: 'red',
                    fontSize: 20
                }
            },
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
                    xAxis: {
                type: 'category',
                name: '时间',
                data: labels
            },
            yAxis: {
                type: 'value',
                name: '利用率'
            },
            series: [{
                name: 'Line 1',
                data: datas,
                smooth:true,
                type: 'bar',
                color: color
            }]
        })
    }


function echarts_pie(chartid, labelname, labels, datas){
        let myChart = echarts.init(document.getElementById(chartid));

        myChart.setOption({
            title : {
                text:labelname, // 主标题
                x:'center', // 主标题位置
                textStyle:{
                    color: 'red', // 颜色
                    fontSize: 20 //字体大小
                }
            },
            toolbox: {
                feature: {
                    saveAsImage: {} //允许保存为图片
                }
            },
            // 鼠标移动上去的提示
            tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
            // 左上角的提示
            legend: {
                orient: 'vertical',
                x: 'left',
                data: labels
            },
            series: [
                {
                    name:labelname, // 本圈的大标题
                    type:'pie', // 饼状图
                    radius: ['50%', '70%'], //小圈 和 大圈的大小
                    avoidLabelOverlap: false,
                    label: {
                        //是否显示名字在侧面
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        // 是否在饼中间显示名字
                        emphasis: {
                            show: true,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    // 是否显示连接饼到名字的线
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: datas
                }
            ]
    })}

//请求URL,获取JSON,并且通过JSON数据绘制各种图表
//URL:请求的URL
//chartid(HTML中canvas标签的名字)
//chart_type:图表类型
//labelname(图表的名称,例如CPU利用率)
function ajax_render_echart(url, chartid) {
            $.getJSON(url,function(data) {//请求URL的JSON,得到数据data,下面是对data的处理
                                            echarts_compound(chartid, data.labelname, data.legends, data.labels, data.datas)
                                          });
            }

function ajax_render_pie(url, chartid) {
            $.getJSON(url,function(data) {//请求URL的JSON,得到数据data,下面是对data的处理
                                            echarts_pie(chartid, data.labelname, data.labels, data.datas)
                                          });
            }