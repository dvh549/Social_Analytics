<template>
<!-- Area Chart -->
    <div class="row">
        
        <div class="col-xl-6 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Topic Keywords</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:600px;">
                    <div class="chart-area">
                        <table>
                            <tr>
                                <th>Topic</th>
                                <th>Related Words</th>
                            </tr>
                            <tr v-for="item in tableData" :key="item">
                                <td>{{item.topic_no}}</td>
                                <td>{{item.topic_words}}</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-6 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Topic Charts</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:600px">
                    <div class="chart-area">
                        <apexchart type="bar" height="550" :options="chartOptions" :series="chartData"></apexchart>
                    </div>
                </div>
            </div>
        </div>
        

    </div>
    <!-- <div class="row" >
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Distribution of Sentiments in Tweets</h6>
                </div>
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                         <apexchart type="bar" height="350" :options="barChartOptions" :series="bar_start"></apexchart>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row" v-if="this.lineData[0].data!=[] && lineChartOptions.xaxis.categories!=[]">

        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Sentiment of Tweets (Weekly)</h6>
                </div>
                <div class="card-body mb-3" style="height:600px">
                    <div class="chart-area">
                       <apexchart type="line" height="500" :options="lineChartOptions" :series="lineData"></apexchart>
                    </div>
                </div>
            </div>
        </div>

    </div> -->



</template>

<script>
// import wordcloud from 'vue-wordcloud'
// import VueWordCloud from 'vuewordcloud';
// import wordcloud from 'vue-wordcloud'
// import Vue3WordCloud from 'vue3-word-cloud';
// import axios from "axios";

export default {
    props: {
        // positiveWordsComponent: Array,
        // negativeWordsComponent: Array,
        // neutralWordsComponent: Array
       
    },
    components: {
        
    },
    data(){
        return{
            chartOptions: {
                chart: {
                type: 'bar',
                height: 350
                },
                plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'
                },
                },
                dataLabels: {
                enabled: false
                },
                
                xaxis: {
                categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
                }
          },
            chartData: [{"data":[116,149,200,573,192,167,104,109,122,260,337,177,138,129,108,533,181,366,154],"name":"negative"},{"data":[101,146,198,497,157,183,116,190,162,316,413,173,142,148,130,514,190,322,160],"name":"positive"},{"data":[47,59,94,175,62,74,42,47,48,108,146,72,75,75,76,246,69,197,64],"name":"neutral"}],
            tableData: [{"topic_no":0,"topic_words":"result,mom,tuesday,like,probably,law,allergy,body,hey,potus"},{"topic_no":1,"topic_words":"china,death,usa,vaccine,done,kill,variant,people,mean,new"},{"topic_no":2,"topic_words":"mask,get,amp,day,time,back,people,school,go,year"},{"topic_no":3,"topic_words":"amp,people,trump,vaccine,dying,mandate,american,mask,keep,died"},{"topic_no":4,"topic_words":"vaccine,vaccinated,pandemic,year,could,chance,take,maryland,fda,variant"},{"topic_no":5,"topic_words":"god,like,vaccine,pandemic,wish,expected,really,fun,one,name"},{"topic_no":6,"topic_words":"sunday,washington,ready,wednesday,july,pandemic,heard,hate,australia,virtual"},{"topic_no":7,"topic_words":"got,booster,like,case,shot,week,get,day,still,last"},{"topic_no":8,"topic_words":"breaking_news,morning,china,rise,wave,white_house,say,fatigue,away,as"},{"topic_no":9,"topic_words":"right,pandemic,catch,government,origin,trump,report,say,need,handling"},{"topic_no":10,"topic_words":"people,death,million,hospital,number,rate,risk,died,many,would"},{"topic_no":11,"topic_words":"gop,china,job,augefortrump,cost,line,government,easy,relief,new"},{"topic_no":12,"topic_words":"amp,biden,tested_positive,would,soon,president,say,first,vaccine,better"},{"topic_no":13,"topic_words":"omicron,year,people,new,long,dc,going,come,time,ivermectin"},{"topic_no":14,"topic_words":"protocol,thought,new,couple,year,show,smell,correct,block,six"},{"topic_no":15,"topic_words":"china,new,want,moment,guy,pandemic,origin,lab,claim,wuhan"},{"topic_no":16,"topic_words":"amp,vaccine,child,see,joebiden,like,would,feel,since,take"},{"topic_no":17,"topic_words":"positive,amp,test,inflation,year,whole,january,say,biden,thing"},{"topic_no":18,"topic_words":"test,today,one,center,free,vaccine,testing,home,march,amp"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicGreenUS")
    //         .then(res=>{
    //         console.log(res.data.message)
    //         // this.chartOptions.xaxis.categories = res.data.message.xaxis
    //         this.chartData = res.data.message.bar_chart
    //         this.tableData = res.data.message.topics
    //         // this.lineChartOptions.xaxis.type = 'datetime';
    //         // this.lineChartOptions.xaxis.categories = res.data.message.dateaxis.map(dateStr => new Date(dateStr).getTime());
            
            
    //         // console.log(res.data.message.wordCloud.positive)
    //         // this.positiveWords= res.data.message.wordCloud.positive
    //         // this.negativeWords= res.data.message.wordCloud.negative
    //         // this.neutralWords= res.data.message.wordCloud.neutral
    //         // console.log(this.positiveWords)
    //         // console.log(this.negativeWords)
    //         // console.log(this.neutralWords)
            

    //         })
    // }


}
</script>

<style scoped>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  
}
</style>

