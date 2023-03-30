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
                categories: [1,2,3,4,5,6,7],
                }
          },
            chartData:[{"data":[2506,2713,3199,1926,1464,4466,2726],"name":"negative"},{"data":[2756,3054,3983,2437,1765,4956,3020],"name":"positive"},{"data":[1583,1594,2433,1299,940,2276,1608],"name":"neutral"}],
            tableData: [{"topic_no":0,"topic_words":"trump,realdonaldtrump,president,american,amp,people,say,white_house,biden,would"},{"topic_no":1,"topic_words":"people,week,time,would,get,relief,vaccine,one,first,today"},{"topic_no":2,"topic_words":"people,vaccine,pandemic,state,dc,say,hospital,health,update,person"},{"topic_no":3,"topic_words":"pandemic,amp,need,would,like,vaccine,crisis,health,donald,economic"},{"topic_no":4,"topic_words":"test,testing,positive,get,result,tested,day,free,dc,vaccine"},{"topic_no":5,"topic_words":"people,like,going,get,go,amp,want,need,one,still"},{"topic_no":6,"topic_words":"case,death,new,day,amp,state,number,million,pandemic,dc"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicPhasesUS")
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

