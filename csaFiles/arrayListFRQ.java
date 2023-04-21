import java.util.*;

public class arrayListFRQ {
  public static class LogMessage {
    private String machineId;
    private String description;

    /** Precondition: message is a valid log message. */
    public LogMessage(String message) {
      int sepInd = message.indexOf(":");
      machineId = message.substring(0, sepInd);
      description = message.substring(sepInd+1);
    }

    /** Returns true if the description in this log message properly contains keyword;
     *          false otherwise
     */
    public boolean containsWord(String keyword) {
      int ind = description.indexOf(keyword);
      while (ind != -1) {
        if ((ind != -1)
        && (ind == 0 || description.substring(ind-1, ind).equals(" "))
        && (ind == description.length() - keyword.length() || description.substring(ind+keyword.length(), ind+keyword.length()+1).equals(" "))) {
          return true;
        }
        ind = description.indexOf(keyword, ind+1);
      }
      return false;
    }

    public String getMachineId() {
      return machineId;
    }

    public String getDescription() {
      return description;
    }
  }

  public static class SystemLog {
    /** Contains all the entries in this system log
     *  Guaranteed not to be null and to contain only non-null entries
     */
    private List<LogMessage> messageList = new ArrayList<LogMessage>();

    /** Removes from the system log all entries whose descriptions properly contain keyword
     *  and returns a list (possible empty) containing the removed entries
     *  Postcondition:
     *   - Entries in the returned list properly contain keyword and
     *     are in the order in which they appeared in the system log.
     *   - The remaining entries in the system log do not properly contain keyword and
     *     are in their original order.
     *   - The returned list is empty if no messages properly contain keyword
     */
    public List<LogMessage> removeMessages(String keyword) {
      ArrayList<LogMessage> retVal = new ArrayList<LogMessage>();
      for (int i = messageList.size()-1; i >= 0; i--) {
        if (messageList.get(i).containsWord(keyword)) {
          retVal.add(messageList.remove(i));
        }
      }
      return retVal;
    }

    public List<LogMessage> getMessageList() {
      return messageList;
    }

    public SystemLog(String[] logs) {
      for (String log : logs) {
        messageList.add(new LogMessage(log));
      }
    }

    // There may be instance variables, constructors, and methods that are not shown
  }
  
  public static class Candidate {
    private int idNumber;
    private String position;
    private double interviewScore;

    /** Constructs a new Candidate object */
    public Candidate (int idNumber, String position, double interviewScore) {
      this.idNumber = idNumber;
      this.position = position;
      this.interviewScore = interviewScore;
      /* implementation not shown */
    }

    /** @return the position for which the candidate is applying */
    public String getPosition() {
      return this.position;
      /* implementation not shown */
    }

    /** @return the candidate's interview score */
    public double getInterviewScore() {
      return this.interviewScore;
      /* implementation not shown */
    }

    // There may be instance variables, constructors, and methods that are not shown

    public String toString() {
      return String.format("Position: %s, Score: %s, ID: %d", position, interviewScore, idNumber);
    }
  }

  public static class CandidatePool {
    /** The list of all candidates */
    private List<Candidate> pool;

    /**Constructs a new CandidatePool object */
    public CandidatePool() {
      pool = new ArrayList<Candidate>();
    }

    /** Adds candidate to the pool
     *  @param candidate the candidate to add to the pool */
    public void addCandidate(Candidate candidate) {
      pool.add(candidate);
    }

    /** returns a list of candidates from the pool that have the same position as position
     * @param position the position of candidates to return
     * @return a list of candidates that have the desired position */
    public List<Candidate> getCandidatesForPosition(String position) {
      List<Candidate> retVal = new ArrayList<Candidate>();
      for (Candidate temp : pool) {
        if (temp.getPosition().equals(position)) {
          retVal.add(temp);
        }
      }
      return retVal;
      /* to be implemented in part(a) */
    }

    /** Returns the candidate from the pool with the highest interview score that
     *  has the same position as position or null if position does not match the
     *  position of any candidate.
     *  @param position the position of the candidate to return
     *  @return the candidate for position with the highest interview score or null */
    public Candidate getBestCandidate(String position) {
      List<Candidate> candidates = getCandidatesForPosition(position);
      if (candidates.size() == 0) {return null;}
      double highestScore = candidates.get(0).getInterviewScore();
      int highestCand = 0;
      for (int cand = 0; cand < candidates.size(); cand++) {
        if (candidates.get(cand).getInterviewScore() > highestScore) {
          highestScore = candidates.get(cand).getInterviewScore();
          highestCand = cand;
        }
      }
      return candidates.get(highestCand);
      /* to be implemented in part (b) */
    }

    /** Removes all candidates from the pool that have the same position as position
     *  @param position the position of candidates to remove from the pool
     * @return the number of candidates removed from the pool */
    public int removeCandidatesForPosition(String position) {
      int count = 0;
      for (int i = pool.size() - 1; i >= 0; i--) {
        if (pool.get(i).getPosition().equals(position)) {
          pool.remove(i);
          count += 1;
        }
      }
      return count;
      /* to be implemented in part (c) */
    }
    

    // There may be instance variables, constructors, and methods that are not shown
  }

  public static void main(String[] args) {
    if (true) { /* first paper */
      String[] logs = new String[]{
        "CLIENT3:security alert - repeated login failures",
        "Webserver:disk offline",
        "SERVER1:file not found",
        "SERVER2:read error on disk DSK1",
        "SERVER1:write error on disk DSK2",
        "Webserver:error on /dev/disk"
      };
      SystemLog sL = new SystemLog(logs);
      for (LogMessage temp : sL.removeMessages("disk")) {
        System.out.println(temp.getDescription());
      }
      System.out.println("|");
      for (LogMessage temp : sL.getMessageList()) {
        System.out.println(temp.getDescription());
      }
    }
    if (true) { /* second paper */
      CandidatePool cands = new CandidatePool();
      cands.addCandidate(new Candidate(0, "accountant", 95.0));
      cands.addCandidate(new Candidate(1, "teller", 85.0));
      cands.addCandidate(new Candidate(2, "accountant", 67.2));
      cands.addCandidate(new Candidate(3, "teller", 66.7));
      cands.addCandidate(new Candidate(4, "lawyer", 75.0));
      cands.addCandidate(new Candidate(5, "accountant", 100.0));
      List<Candidate> testVal = cands.getCandidatesForPosition("accountant");
      Candidate bestCand = cands.getBestCandidate("teller");
      System.out.println(testVal);
      System.out.println(bestCand);
      int candsRemoved = cands.removeCandidatesForPosition("teller");
      System.out.println(candsRemoved);
    }
  }
}
