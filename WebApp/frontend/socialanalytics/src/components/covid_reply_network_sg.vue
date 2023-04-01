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
                            <strong>Do take note this is an analysis of quote/reply network</strong>
                            <br/>

                            <span style="color:orange">“mrbrown”</span> - pseudonym of Lee Kin Mun, a Singaporean blogger, writer, and internet personality. He is known for his humorous commentary on current affairs and social issues in Singapore.  He has high in-degree centrality, which suggests that his opinions are valued by his followers. He discussed mostly about the Covid-19 situation in Hong Kong and in Singapore. The reason for his high in-degree centrality could be his humorous and witty commentary on current events. The sentiment towards the topics discussed had a balance of positive, neutral, and negative reactions.  Our model predicted mainly “Fake” news, likely due to his writing style that includes informal language and sometimes sarcasm. Despite this, his tweets generally provide factual information, and he can be ideal to spread information and opinions to those who appreciate his humour and commentary. 
                            <br/>
                            <br/>

                             <span style="color:purple">“malaysia_covid”</span> - It has high in-degree centrality in a reply network, meaning that it receives a lot of replies and mentions from other users. Malaysia_covid discussed mostly about the Covid-19 situation in Malaysia, posting statistics on daily cases, vaccination, and flight information for various cities. The sentiment toward the topics discussed had a balance of positive, neutral, and negative reactions. Our Fake News model classifies his tweets as mainly “Fake”, however in our manual analysis, it might be due to the use of Malaysian state names in his tweets, which may not be accurately captured by the model (that was trained on US related information). The tweets are mainly updates on the situation in Malaysia. Malaysia_covid’s extensive influence and reach in the Reply Network, with 25,000 followers, is likely to have a positive impact on the dissemination of reliable and valuable information about the Covid-19 situation in Malaysia. As such, malaysia_covid is important to transmit reliable information to those interested in the Covid-19 situation in Malaysia. 
                            <br/>
                            <br/>

                            <span style="color:green">“rodahidup”</span> - Based on his profile, he appears to be a Malaysian living or working in Singapore and has high out-degree centrality, indicating his involvement in many topics surrounding the Covid-19 situation in Singapore and Hong Kong and the vaccine situation. He actively initiates conversations and tends to reply to news related to the pandemic. The sentiment towards the topics discussed had a balance of positive, neutral, and negative reactions. Our model predicted mainly “Fake” news, but on manual analysis of his tweets, they are primarily his opinions which are subjective. However, his influence is limited as he has a small following of 2300 users. 
                            <br/>
                            <br/>

                            <span style="color:red">“bobby_the_great”</span> - He has high out-degree centrality which indicates that he posts many tweets and responds to many tweets from other users. He primarily discusses the dire situation in China and the protests that were happening. The sentiment toward the topics discussed had a balance of positive, neutral, and negative reactions. Our model predicted mainly “Fake” news but a manual analysis of his tweets revealed that they are primarily his subjective opinions. Despite his active participation, his low number of followers (199) indicates that he has limited reach and influence in the network. 
                            <br/>
                            <br/>
                        
                            <span style="color:pink">“traintheteacher”</span> - Stephanie Thompson, a teacher based in Romania with high betweenness centrality. She was born in Canada, grew up in New Zealand and taught in South Korea and Singapore previously. During the first few months of Covid-19, she lived in Singapore. She discussed mostly about how to manage students with Covid-19 measures put in place. She also mentioned about different experiences in different countries, such as Singapore starting to deal with the pandemic earlier than New Zealand, and that Romania has a higher rate of transmission than New Zealand. Her followers are likely her connections that she made from the various countries she has been in, and she is a cut-point that connects these different communities together. The sentiment towards the topics discussed had a balance of positive and negative reactions with regards to her sharing her experience. Manual analysis of her tweets suggests that she is sharing her personal experiences and is not spreading misinformation. Her tweets would likely benefit other teachers looking for insights on how to manage their classrooms during the pandemic, and individuals who are keen to learn about the different measures taken in different countries in response to the pandemic. As such, her tweets may be valuable to her immediate network, but she may not have a significant influence in the wider social network. 
                            <br/>
                            <br/>

                            <span style="color:grey">“daphnemaia”</span> - Daphne Maia Loo, a strength and nutrition coach, and an ex-social media consultant, has high betweenness centrality. This may be attributed to her past controversy and online exposure as she may have attracted people from different backgrounds and communities to follow her. In 2019, she was featured on several news platforms like AsiaOne, GoodyFeed, and Mashable SEA, for several issues such as her losing 9kg in 3 months and garnering attention and followers online as she documents her weight-loss journey on social media, and for calling out another influencer who sought a free personal trainer and requested the trainer to even pay her for the training. She discussed mostly her personal experiences during the acute phase in Singapore. The sentiment towards the topics discussed had a balance of positive and negative reactions. Our model predicted mainly “Fake” news; however, her tweets were mainly about her experiences. She may not be the ideal source to spread concrete/useful information to a larger network. 
                            <br/>
                            <br/>

                            <span style="color:brown">“DanOgunshakin”</span> - Dan Ogunshakin, a BBC Journalist with high betweenness centrality. Prior to his current role, he worked in Singapore for Fox Sports Asia. He is based in London and worked in Thailand, Australia, and Malaysia previously as a dive instructor. He discussed mostly about the Covid-19 situation in the UK and provided his opinions on it. His followers are likely his connections that he made from the various countries he has been in, and he is a cut-point that connects these different communities together. The sentiment towards the topics discussed had a balance of positive and negative reactions. Our model predicted mainly “Fake” news; however, his tweets were mainly his opinions. He is highly critical of the UK government's handling of the pandemic, with tweets such as “Good luck to everyone back in the UK going back into lockdown. I'm sorry your government has utterly failed you at every turn. I just hope that everyone adheres to the rules (and ignores the usual covid deniers) as much as it may suck”. As such, he may not be the ideal source to spread concrete information to the larger network, although his tweets reflect some of the prevailing sentiments towards the pandemic in the UK. 
                            <br/>
                            <br/>

                            All centrality measures were calculated using NetworkX. Visualisations were derived from Gephi where node importance was configured based on the sum of in and out degrees. However, it should be noted that in the reply network, those with high in-degrees will not be as “big” in size as those with high out-degrees as there are many more replies (source) than those receiving replies (target). E.g., “mrbrown” has a high in-degree as he has a large following (416k followers) and receives replies from other users. “_rodahidup”, on the other hand, is a very active user with high out-degree as he frequently replies to other users’ tweets, actively participating in various discussions & conversations. “_rodahidup” is actively engaging in conversations with a wider range of users from different communities, while “mrbrown” is the focus of conversations initiated by his followers. As such, “_rodahdup” has a greater ability to initiate and contribute to conversations with a wider range of users. 
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
import jsonData from "../assets/nodeJsonCovidReplySG.json"
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
        betweeness:{'traintheteacher': "2.348885894059374e-06",
                    'daphnemaia': "2.055275157301952e-06",
                    'TwiddyBird62': "1.174442947029687e-06",
                    'DanOgunshakin': "1.174442947029687e-06",
                    'dwallbank': "8.808322102722652e-07",
                    'Sgboy01': "8.808322102722652e-07",
                    'AudiKhalid': "5.872214735148435e-07",
                    'sarahcoldheart': "5.872214735148435e-07",
                    'eddydaud':" 5.872214735148435e-07",
                    'societyofsnobs': "2.9361073675742175e-07"
                    },
        closeness:{'mrbrown': 0.0032502708559046588,
                    'realDonaldTrump': 0.0032502708559046588,
                    'malaysia_covid': 0.0021668472372697724,
                    'MothershipSG': 0.0021668472372697724,
                    'AudiKhalid': 0.0016928494041170098,
                    'sarahcoldheart': 0.0016928494041170098,
                    'tanhuiyi': 0.0016251354279523294,
                    'SCMPNews': 0.001218851570964247,
                    'mintea': 0.001218851570964247,
                    'AdamFlinter': 0.001218851570964247
                    },
        indegree:{'mrbrown': 0.0032502708559046583,
                'realDonaldTrump': 0.0032502708559046583,
                'malaysia_covid': 0.0021668472372697724,
                'MothershipSG': 0.0021668472372697724,
                'sarahcoldheart': 0.0016251354279523292,
                'tanhuiyi': 0.0016251354279523292,
                'AudiKhalid': 0.0010834236186348862,
                'business': 0.0010834236186348862,
                'catturd2': 0.0010834236186348862,
                'sheryl0_C': 0.0010834236186348862
                },
        outdegree:{'_rodahidup': 0.020043336944745395,
                    'bobby_the_great': 0.010834236186348862,
                    'shuklap': 0.010834236186348862,
                    'Firehorse77': 0.009750812567713976,
                    'mulletrider': 0.00866738894907909,
                    'thebendingone': 0.008125677139761646,
                    'JosephJohnAdam1': 0.007583965330444203,
                    'jaschintaz': 0.006500541711809317,
                    'DanielSadhu': 0.005958829902491874,
                    'sufw': 0.005417118093174431,
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
