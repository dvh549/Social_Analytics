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
                categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
                }
          },
            chartData:[{"data":[142,166,112,128,141,131,118,145,173,155,136,119,117,135,149,131,128],"name":"negative"},{"data":[198,200,147,200,204,153,178,197,211,208,169,178,161,205,217,204,263],"name":"positive"},{"data":[132,174,101,121,127,103,105,123,190,165,101,117,114,111,122,131,128],"name":"neutral"}],
            tableData: [{"topic_no":0,"topic_words":"singapore,get,know,year,one,need,like,income,feel,old"},{"topic_no":1,"topic_words":"singapore,lockdown,new,stayhome,vaccine,case,worker,get,situation,sgunited"},{"topic_no":2,"topic_words":"home,singapore,day,news,via,pandemic,like,abc,whole,stayhome"},{"topic_no":3,"topic_words":"singapore,want,american,please,people,one,make,wall,mexico,border"},{"topic_no":4,"topic_words":"case,total,singapore,death,new,today,infection,testing,update,bangladesh"},{"topic_no":5,"topic_words":"day,singapore,say,week,virus,call,alcohol,doctor,people,come"},{"topic_no":6,"topic_words":"singapore,china,first,government,home,outbreak,singaporean,india,new,crisis"},{"topic_no":7,"topic_words":"singapore,pandemic,home,stay,spread,due,circuit_breaker,safe,affected,situation"},{"topic_no":8,"topic_words":"time,world,work,little,fight,get,wait,home,normal,life"},{"topic_no":9,"topic_words":"singapore,safe,lockdown,go,amp,world,please,would,time,via"},{"topic_no":10,"topic_words":"like,people,go,singapore,see,family,come,may,indian,end"},{"topic_no":11,"topic_words":"singapore,time,amp,world,case,month,see,make,still,started"},{"topic_no":12,"topic_words":"home,pandemic,circuitbreaker,need,singapore,let,mask,stay,one,today"},{"topic_no":13,"topic_words":"may,people,home,singapore,one,month,safe,work,health,many"},{"topic_no":14,"topic_words":"singapore,stayhome,day,home,stayathome,circuitbreaker,time,need,month,help"},{"topic_no":15,"topic_words":"singapore,day,amp,need,time,friend,see,one,first,end"},{"topic_no":16,"topic_words":"case,new,singapore,home,time,stay,amp,lockdown,people,spread"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicCB")
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

