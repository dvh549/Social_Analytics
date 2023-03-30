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
            chartData:[{"data":[13,49,25,34,23,31,20,53,26,62,27,71,49,32,44,57,27,24],"name":"negative"},{"data":[37,61,40,42,40,43,29,77,34,98,29,106,68,43,82,87,33,36],"name":"positive"},{"data":[10,31,20,27,22,19,11,34,23,33,21,82,42,21,32,40,20,26],"name":"neutral"}],
            tableData: [{"topic_no":0,"topic_words":"everyone,keep,get,via_youtube,outbreak,time,safe,last,online,year"},{"topic_no":1,"topic_words":"singapore,need,please,like,go,china,let,day,news,say"},{"topic_no":2,"topic_words":"singapore,safe,stay,people,say,case,home,china,many,one"},{"topic_no":3,"topic_words":"singapore,mask,would,outbreak,one,day,need,country,may,pandemic"},{"topic_no":4,"topic_words":"china,outbreak,singapore,due,news,get,mar,people,uk,better"},{"topic_no":5,"topic_words":"singapore,case,spread,still,amp,new,response,people,like,news"},{"topic_no":6,"topic_words":"singapore,love,cure,like,sg,time,pandemic,well,spread,great"},{"topic_no":7,"topic_words":"singapore,case,local,amp,outbreak,new,help,home,like,stay"},{"topic_no":8,"topic_words":"one,stay,china,even,singapore,really,case,going,like,getting"},{"topic_no":9,"topic_words":"singapore,people,home,go,need,time,government,good,change,racist"},{"topic_no":10,"topic_words":"fuck,singapore,watch,case,job,way,community,great,next,air"},{"topic_no":11,"topic_words":"singapore,home,mainemendoza,stay,going,ingat_sa,time,everyone,take,good"},{"topic_no":12,"topic_words":"situation,virus,china,case,singapore,country,novel,update,outbreak,test"},{"topic_no":13,"topic_words":"time,people,one,singapore,china,need,got,better,world,another"},{"topic_no":14,"topic_words":"singapore,case,new,time,confirmed,first,via,death,help,two"},{"topic_no":15,"topic_words":"singapore,china,amp,wuhan,people,mask,virus,outbreak,world,new"},{"topic_no":16,"topic_words":"singapore,news,good,via,outbreak,world,case,update,stay,spread"},{"topic_no":17,"topic_words":"march,singapore,world,go,take,virus,economic,via,safe,lockdown"}]
        }

  }, 
    // mounted(){
    //     axios.get("http://127.0.0.1:5000/getTopicStart")
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

