import React, { Component } from 'react';
import { StyleSheet, View, Dimensions, Image, Vibration, Text, PermissionsAndroid,} from 'react-native';
import Voice from '@react-native-voice/voice';
import Tts from 'react-native-tts';
import TrackPlayer from 'react-native-track-player';

import {
  LongPressGestureHandler,
  TapGestureHandler,
  ScrollView,
  State,
} from 'react-native-gesture-handler';

import { LogBox } from 'react-native';
LogBox.ignoreLogs(['new NativeEventEmitter']); // Ignore log notification by message
LogBox.ignoreAllLogs();

const widthPhone = Dimensions.get("window").width;
const heightPhone = Dimensions.get("window").height;

const story = "Ngày xửa, ngày xưa, giữa mùa đông giá rét, tuyết rơi trắng như bông có một bà hoàng hậu ngồi khâu bên cửa sổ khung gỗ mun, bà mải nhìn tuyết nên kim đâm phải tay, ba giọt máu rơi xuống tuyết. Thấy máu đỏ pha lẫn tuyết trắng thành một màu tuyệt đẹp, bà nghĩ bụng: “Ước gì ta đẻ được một người con gái, da trắng như tuyết, môi đỏ như máu và tóc đen như gỗ khung cửa này”Sau đó ít lâu, bà đẻ một cô gái trắng da như tuyết, môi đỏ như máu và tóc đen như mun; vì vậy bà đặt tên con là Bạch Tuyết. Bạch Tuyết vừa ra đời thì mẹ chết. Một năm sau, vua lấy vợ khác. Bà này đẹp lắm nhưng kiêu căng tự phụ, độc ác và không muốn ai đẹp bằng mình. Bà có một cái gương thần, khi soi, bà hỏi:"

class MultiTap extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
        numberOfTouches: 2,
    };
  }

  static defaultProps = {
    onPress: () => null,
    numberOfTouches: 2,
    delay: 10,
  }

  startPress = null;

  onStartShouldSetResponder = (evt) => {
    if (evt.nativeEvent.touches.length === this.state.numberOfTouches) {
      this.startPress = Date.now();
      print("aaaaaaaaaaaaaaaaaaaaaa")
      return true;

    }

    return false;
  }

  onResponderRelease = () => {
    print("bbbbbbbbbbbbbbbbbbbbbb")
    const now = Date.now();
    if (this.startPress && now - this.startPress > this.props.delay) {
      this.props.onPress();
    }
    this.startPress = null;
  }

  render() {
    return (
      <View
        onStartShouldSetResponder={this.onStartShouldSetResponder}
        onResponderRelease={this.onResponderRelease}
      >
        {this.props.children}
      </View>
    );
  }
}

export class PressBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            pitch : '',
            error: '',
            end: '',
            started: '',
            results: [],
            ttsResults: '',
            partialResults: [],
            story:['alice ở xứ sở thần tiên','bạch tuyết và bảy chú lùn','nàng tiên cá'],
        };

        Voice.onSpeechStart = this.onSpeechStart;
        Voice.onSpeechEnd = this.onSpeechEnd;
        Voice.onSpeechError = this.onSpeechError;
        Voice.onSpeechResults = this.onSpeechResults;
        Voice.onSpeechPartialResults = this.onSpeechPartialResults;
        Voice.onSpeechVolumeChanged = this.onSpeechVolumeChanged;
        this.requestExternalStorageRead();
        this.requestMic();
    }

    componentDidUpdate() {
      Voice.onSpeechStart = this.onSpeechStart;
      Voice.onSpeechEnd = this.onSpeechEnd;
      Voice.onSpeechError = this.onSpeechError;
      Voice.onSpeechResults = this.onSpeechResults;
      Voice.onSpeechPartialResults = this.onSpeechPartialResults;
      Voice.onSpeechVolumeChanged = this.onSpeechVolumeChanged;
      this.requestExternalStorageRead();
      this.requestMic();

      // Tts.addEventListener(
      //   'tts-start',
      //   (_event) => this.setState({ttsStatus: 'started'})
      // );
      // Tts.addEventListener(
      //   'tts-finish',
      //   (_event) => {
      //     this.setState({ttsStatus: 'finished'})
      //   }
      // );
      // Tts.addEventListener(
      //   'tts-cancel',
      //   (_event) => this.setState({ttsStatus: 'cancelled'})
      // );

      return () => {
        //destroy the process after switching the screen
        Voice.destroy().then(Voice.removeAllListeners);
        
        // Tts.removeEventListener(
        //   'tts-start',
        //   (_event) => this.setState({ttsStatus: 'started'})
        // );
        // Tts.removeEventListener(
        //   'tts-finish',
        //   (_event) => this.setState({ttsStatus: 'finished'})
        // );
        // Tts.removeEventListener(
        //   'tts-cancel',
        //   (_event) => this.setState({ttsStatus: 'cancelled'})
        // );
      };
    }

    
    async requestExternalStorageRead() {
      try {
        const granted = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.READ_EXTERNAL_STORAGE,
          {
            'title': 'Cool App ...',
            'message': 'App needs access to external storage'
          }
        );
  
        return granted == PermissionsAndroid.RESULTS.GRANTED
      }
      catch (err) {
        //Handle this error
        return false;
      }
    }

    async requestMic() {
      try {
        const granted = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.RECORD_AUDIO,
          {
            title: 'Permissions for record audio',
            message: 'Give permission to your device to record audio',
          },
        );
        return granted == PermissionsAndroid.RESULTS.GRANTED
      }
      catch (err) {
        return false;
      }
    }

    onSpeechStart = (e) => {
        //Invoked when .start() is called without error
     //   console.log('onSpeechStart: ', e);
        this.setState({started: '√'});
    };
    
    onSpeechEnd = (e) => {
        //Invoked when SpeechRecognizer stops recognition
        console.log('ornSpeechEnd: ', e);
        this.setState({end: '√'});
    };
    
    onSpeechError = (e) => {
        //Invoked when an error occurs.
        console.log('onSpeechError: ', e);
        this.setState({ error: JSON.stringify(e.error)});
    };
    
    onSpeechResults = (e) => {
        //Invoked when SpeechRecognizer is finished recognizing
       // console.log('onSpeechResults: ', e);
        this.setState({results: e.value});
        let spoken  = 0;
        for (i = 0; i<e.value.length; i++) {
          spoken = e.value[i].toLowerCase();
          if(spoken.includes('danh sách')){
            this.state.story.map((result) => {
              Tts.speak(result);
            });
            break;
          }
          if(spoken.includes('xứ sở thần tiên')){
            TrackPlayer.setupPlayer().then(async () => {
              // Adds a track to the queue
              await TrackPlayer.add({
                id: '1',
                url: '/storage/emulated/0/sound/alice-in-wonderland/19573-01.mp3',
                title: 'Alice in Wonderland, Chapter 1: Down the Rabbit-Hole',
                artist: 'Lewis Carroll',
              });
           
              // Starts playing it
              TrackPlayer.play();
           
          });
            
            break;
          }
          if(spoken.includes('chương 3')){
            TrackPlayer.reset();
            // Adds a track to the queue
            TrackPlayer.add({
                id: '3',
                url: '/storage/emulated/0/sound/alice-in-wonderland/19573-03.mp3',
                title: 'Alice in Wonderland, Chapter 3',
                artist: 'Lewis Carroll',
              });
           
              // Starts playing it
              TrackPlayer.play();
            
            break;
          }
          if(spoken.includes('bạch tuyết')){
            Tts.speak(story);
            break;
          }
          if(spoken.includes('chào')){
            Tts.speak("Chào Quyết, hiện không có câu chuyện nào đang được kể. Chúng tôi hiện có ba câu chuyện dành cho bạn.");
            break;
          }
          if(spoken.includes('kết thúc')){
            TrackPlayer.reset();
            Tts.stop();
            break;
          }
          if(spoken.includes('tạm dừng')){
            TrackPlayer.pause();
            break;
          }
          if(spoken.includes('tiếp tục')){
            TrackPlayer.play();
            break;
          }
        }
      this.setState({stopped: true});
    };
    
    onSpeechPartialResults = (e) => {
        //Invoked when any results are computed
      //  console.log('onSpeechPartialResults: ', e);
        this.setState({partialResults: e.value});
    };
    
    onSpeechVolumeChanged = async (e) => {
        //Invoked when pitch that is recognized changed
        //console.log('onSpeechVolumeChanged: ', e);
        this.setState({pitch: e.value});
        
    };

    _onHandlerStateChange = event => {
        console.log("voice start!")
        Vibration.vibrate();
        TrackPlayer.pause();
        Tts.stop();
        this.startRecognizing();
        this.setState({stopped: false});
    }

    // };
    // _onHandlerStateChange = event => {
    //     alert("I'm being pressed for so long");
    // };

    _onDoubleTap = event => {
      if (event.nativeEvent.state === State.ACTIVE) {
        alert("ccccccccccccccccc");
      }
    }

  startRecognizing = async () => {
    try {
        await Voice.start('vi');
        this.setState({pitch: ''});
        this.setState({error: ''});
        this.setState({started: ''});
        this.setState({result: []});
        this.setState({partialResults: []});
        this.setState({end: ''});
      } catch (e) {
        //eslint-disable-next-line
        console.error(e);
      }
  }

  render() {
    return (
      <MultiTap onPress={this._onHandlerStateChange}>
      <View style={styles.box}>
                <Image source={require('./mic.png')} style={styles.img}  />
                {console.log(this.state.results)}
                {this.state.results.map((result, index) => {return (
                  <Text style={{size: 30}}>{result}</Text>
                )}
                )}
            </View>
    </MultiTap>
    );
  }
}

export default class Example extends Component {
  render() {
    return (
      <ScrollView style={styles.scrollView}>
        <PressBox />
      </ScrollView>
    );
  }
}

const styles = StyleSheet.create({
  scrollView: {
    flex: 1,
  },
  box: {
    width: widthPhone,
    height: heightPhone-50,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'white',
    zIndex: 200,
  },
  img: {
    width: 50,
    height: 50,
  }
});