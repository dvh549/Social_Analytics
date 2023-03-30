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
                categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                }
          },
            chartData:[{"data":[175,145,758,135,194,155,433,171,248,141,502,227,275,215,162],"name":"negative"},{"data":[204,155,868,155,183,180,506,178,360,142,544,257,301,261,172],"name":"positive"},{"data":[143,102,487,125,140,163,368,107,230,99,312,197,226,172,119],"name":"neutral"}],
            tableData: [{"topic_no":0,"topic_words":"get,going,people,let,year,next,health,information,free,everything"},{"topic_no":1,"topic_words":"case,update,amid,number,dc,county,total,city,diagnosed,first"},{"topic_no":2,"topic_words":"amp,people,get,say,pandemic,trump,want,like,need,one"},{"topic_no":3,"topic_words":"trump,response,bill,house,global,plan,vote,senate,crisis,get"},{"topic_no":4,"topic_words":"trump,president,state,said,say,health,emergency,italy,breaking,people"},{"topic_no":5,"topic_words":"school,one,kid,press,meal,student,started,confirms,employee,tomorrow"},{"topic_no":6,"topic_words":"china,virus,chinese,amp,health,realdonaldtrump,issue,president,public,outbreak"},{"topic_no":7,"topic_words":"dc,conference,washington,corona,due,virus,briefing,stock,office,md"},{"topic_no":8,"topic_words":"like,people,going,really,china,need,would,see,getting,say"},{"topic_no":9,"topic_words":"case,first,test,confirmed,new,positive,say,people,state,report"},{"topic_no":10,"topic_words":"spread,back,work,market,country,community,time,people,thread,panic"},{"topic_no":11,"topic_words":"may,cancelled,go,show,would,could,ebola,guess,day,home"},{"topic_no":12,"topic_words":"amp,school,dc,people,student,know,closed,please,need,wash_hand"},{"topic_no":13,"topic_words":"people,case,day,got,wuhan,infected,country,epidemic,could,saying"},{"topic_no":14,"topic_words":"flu,vaccine,pandemic,time,kill,full,like,way,cdc,think"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicStartUS")
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

