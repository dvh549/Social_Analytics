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
                categories: [1,2,3,4,5,6,7,8,9,10,11],
                }
          },
            chartData:[{"data":[232,105,121,125,92,75,105,215,155,171,127],"name":"negative"},{"data":[256,146,163,175,133,119,124,249,211,278,157],"name":"positive"},{"data":[160,112,121,133,89,74,73,153,215,136,107],"name":"neutral"}],
            tableData:[{"topic_no":0,"topic_words":"people,singapore,time,case,death,vaccine,still,like,first,get"},{"topic_no":1,"topic_words":"test,singapore,get,positive,many,case,new,time,via,amp"},{"topic_no":2,"topic_words":"amp,day,friend,test,today,singapore,one,thing,year,time"},{"topic_no":3,"topic_words":"singapore,pandemic,time,year,china,live,via,like,see,case"},{"topic_no":4,"topic_words":"singapore,enough,test,country,testing,get,happening,new,year,free"},{"topic_no":5,"topic_words":"world,people,singapore,know,day,first,american,virus,outbreak,case"},{"topic_no":6,"topic_words":"vaccine,singapore,trump,year,news,via,people,pandemic,trial,election"},{"topic_no":7,"topic_words":"go,vaccine,amp,like,people,year,really,back,time,got"},{"topic_no":8,"topic_words":"uk,singapore,phase,pandemic,day,country,measure,number,news,case"},{"topic_no":9,"topic_words":"singapore,case,new,day,one,get,community,cluster,die,need"},{"topic_no":10,"topic_words":"singapore,case,home,new,death,still,day,work,virus,report"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicPhases")
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

