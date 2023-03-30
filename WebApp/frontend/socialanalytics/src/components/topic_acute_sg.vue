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
                categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                }
          },
            chartData:[{"data":[31,55,21,45,30,43,30,24,60,18,30,52,19,44,11,20,26,50],"name":"negative"},{"data":[26,67,34,71,30,61,31,31,77,31,36,80,11,50,30,28,43,59],"name":"positive"},{"data":[14,77,17,26,13,87,19,23,34,11,16,31,18,29,15,26,13,30],"name":"neutral"}],
            tableData: [{"topic_no":0,"topic_words":"like,long,month,year,day,test,death,many,feel,risk"},{"topic_no":1,"topic_words":"time,need,got,amp,take,work,people,booster,even,getting"},{"topic_no":2,"topic_words":"singapore,got,get,year,people,rule,like,new,say,omicron"},{"topic_no":3,"topic_words":"singapore,china,wave,restriction,without,flight,booster,vaccine,malaysia,first"},{"topic_no":4,"topic_words":"singapore,one,long,well,feel,still,need,safe,restriction,want"},{"topic_no":5,"topic_words":"singapore,year,life,people,see,got,even,time,test,dun"},{"topic_no":6,"topic_words":"singapore,day,also,live,right,people,thing,still,year,gt"},{"topic_no":7,"topic_words":"really,get,one,singapore,time,day,say,bad,still,life"},{"topic_no":8,"topic_words":"singapore,time,first,got,people,amp,since,think,get,city"},{"topic_no":9,"topic_words":"people,issue,also,singapore,right,home,let,mask,joe_rogan,still"},{"topic_no":10,"topic_words":"singapore,people,test,think,go,management,issue,better,please,got"},{"topic_no":11,"topic_words":"singapore,people,day,best,good,family,got,thing,time,like"},{"topic_no":12,"topic_words":"case,new,singapore,death,report,omicron_infection_confirmed,million,reported,patient,still"},{"topic_no":13,"topic_words":"people,everyone,zero,singapore,via,amazing,amp,one,china,restriction"},{"topic_no":14,"topic_words":"get,still,year,people,recover,home,last,mask,health,know"},{"topic_no":15,"topic_words":"omicron,singapore,case,time,variant,test,positive,home,daily,new"},{"topic_no":16,"topic_words":"singapore,year,see,people,still,yes,get,day,lockdown,china"},{"topic_no":17,"topic_words":"get,like,work,still,time,back,feel,use,got,year"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicAcute")
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

