<template>
<!-- Area Chart -->
    <div class="row">
        
        <div class="col-xl-6 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Social Network Quote Network</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <div ref="graph" style="height:600px"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-6 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Analysis</h6>
                </div>
                <div class="card-body" style="height:700px; overflow-y: scroll;">
                    <div class="chart-area">
                        <p>
                            <strong>Do take note this is an analysis of quote/reply network </strong>
                            <br/>


                            <span style="color:orange;">"DTrain”</span> - Dennis Chiuten has high betweenness centrality. Upon further research, he is a native New Yorker, and he moved to Singapore to start a career in investment banking. As a result, he can act as a bridge between two communities of people, his followers in the United States and his followers in Singapore. He discussed about the Covid-19 situation globally and provided his opinions, including differences between how Asian countries and Western countries managed Covid-19 issues such as mask-wearing. The sentiment towards the topics discussed had a balance of positive and negative reactions. Our model predicted mainly “Fake” news however his tweets were mainly his opinions. While DTrain's opinions may not necessarily be considered "Fake" news, they are subjective and may not be backed by scientific evidence or expert consensus. For instance, one of his tweets reads, “Strike me down, coronavirus, and I will become more powerful than you could ever possibly imagine”. This tweet may be interpreted differently by different people and may not be relevant to everyone. As an information broker with a relatively smaller reach of 3000 followers, DTrain may not be ideal to spread information to large groups of people. 
                            <br/>
                            <br/>
                            <span style="color:purple;">“BogdziewiczM”</span> - Magdalena Bogdziewicz has high betweenness centrality as the Ambassador of Poland to Singapore. Her position and expertise likely contributed to her bridging the people in Poland and Singapore. As an ambassador, she likely has credibility which makes her a trustworthy source of information. On Twitter, she mainly discussed about the Covid-19 situation in Poland and promoted exchanges between the two countries, connecting people interested in these topics. The sentiment towards the topics discussed was mostly positive. However, she may have a limited reach due to her small following of 495. Nevertheless, as the Ambassador of Poland to Singapore, BogdziewiczM likely has access to valuable information and insights that could be benefit her followers and those interested in Poland-Singapore relations. As such, BogdziewiczM can be considered a spreader of accurate and useful information. 
                            <br/>
                            <br/>
                            <span style="color:green;">“DannyQuah”</span> - Danny Quah is an NUS Economics Professor and Dean with high betweenness centrality. This is likely due to his position in the academic field as he is well-connected with other researchers and experts in his field. The main topics he discussed were mostly the Covid-19 vaccine, booster shots, and the reopening of economies after a lockdown in countries like Singapore and France. The sentiment towards the topics discussed had a balance of positive and negative reactions. Our model predicted mainly “Fake” news however his tweets were mainly his opinions and experiences. As an academic and expert in the field, DannyQuah may be a reliable source of useful information for his followers and others interested in his area of expertise. Therefore, he could be ideal for passing on information in a social network, particularly among those interested in the relationship between Covid-19 and economics. 
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Betweenness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in betweeness" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Closeness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in closeness" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>In Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in indegree" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Out Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in outdegree" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        
    </div>


    



</template>

<script>
import 'vis-network/styles/vis-network.css'
import { Network } from "vis-network/peer/esm/vis-network";
import { DataSet } from "vis-data/peer/esm/vis-data"
import jsonData from "../assets/nodeJsonCoronaQuoteSG.json"
// import {CovidNode} from '../config.js'
export default {
    props: {
        // positiveWordsComponent: Array,
        // negativeWordsComponent: Array,
        // neutralWordsComponent: Array
       
    },
    components: {
        // SocialNetwork
        // Network
    },
    data(){
        return{
        network:null,
        // edges: 
        betweeness:{'danibogo': 0.0,
                    'OficinadaNet': 0.0,
                    'msmsaifullah': 0.0,
                    'TheEconomist': 0.0,
                    'herniepotter': 0.0,
                    'k4tt76d': 0.0,
                    'ChannelNewsAsia': 0.0,
                    'meghamerlyn': 0.0,
                    'IndiaToday': 0.0,
                    'RanaAyyub': 0.0,
                    },
        closeness:{'straits_times': 0.018315018315018316,
                    'ChannelNewsAsia': 0.014652014652014652,
                    'realDonaldTrump': 0.01098901098901099,
                    'Reuters': 0.01098901098901099,
                    'WHO': 0.01098901098901099,
                    'globaltimesnews': 0.007326007326007326,
                    'FinancialTimes': 0.007326007326007326,
                    'CBSNews': 0.007326007326007326,
                    'SCMPNews': 0.007326007326007326,
                    'CNBC': 0.007326007326007326,
                    },
        indegree:{'straits_times': 0.018315018315018316,
                    'ChannelNewsAsia': 0.014652014652014652,
                    'realDonaldTrump': 0.01098901098901099,
                    'Reuters': 0.01098901098901099,
                    'WHO': 0.01098901098901099,
                    'globaltimesnews': 0.007326007326007326,
                    'FinancialTimes': 0.007326007326007326,
                    'CBSNews': 0.007326007326007326,
                    'SCMPNews': 0.007326007326007326,
                    'CNBC': 0.007326007326007326,
                },
        outdegree:{'leejanhau': 0.0879120879120879,
                    'jwalantudesai': 0.02564102564102564,
                    'msmsaifullah': 0.021978021978021976,
                    'jimmyjemii': 0.018315018315018316,
                    'izreloaded': 0.018315018315018316,
                    'ajaymodi81': 0.018315018315018316,
                    'Godliketrader': 0.014652014652014652,
                    'dwallbank': 0.014652014652014652,
                    'NHHungerford': 0.014652014652014652,
                    'AliIsBk1': 0.010989010989010988,
                    }

        }
  }, 
    mounted() {
        const container = this.$refs.graph
        var nodes = new DataSet(jsonData.nodes)
        var edges = new DataSet(jsonData.edges)

        const data = {
        nodes: nodes,
        edges: edges
        }
        const options = {
             interaction: {
                navigationButtons: true,
                zoomView: true, // Enable zooming
                dragView: true, // Enable panning 
            },
            layout:{
                improvedLayout:false
            },
             nodes: {
                size: 10
            }
            

        }
        console.log("HERE")
        // new Network(container, data, options)
        var network = new Network(container, data, options)
        this.network= network
        // this.zoomToNode(2);
            
        

    },
    methods: {
        //  zoomToNode(nodeId) {
            
        //         var position = this.network.getPositions()[nodeId];
        //         this.network.focus(2,{
        //             position: {x:position.x, y:position.x},
        //             offset: position,
        //             scale: 1,
        //             locked: false,
        //         });
           
        // },
        
    }


}
</script>

<style scoped>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    
    }
</style>
