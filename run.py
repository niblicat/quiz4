import module_1.chorus as Chorus
import module_1.pre_chorus as PreChorus
import module_2.bridge as Bridge
import module_2.interlude as Interlude
import module_2.outro as Outro
import module_3.verse1 as VerseFirst
import module_3.verse2 as VerseSecond

def allstar():
    # shrek
    VerseFirst.Song()
    PreChorus.Song()
    Chorus.Song()
    VerseSecond.Song()
    Chorus.Song()
    Interlude.Song()
    Chorus.Song()
    Bridge.Song()
    PreChorus.Song()
    Chorus.Song()
    Outro.Song()

if (__name__ == "__main__"):
    allstar()